from sqlalchemy.engine import base
from sqlalchemy.engine import url as _url
from sqlalchemy.engine.mock import create_mock_engine
from sqlalchemy import event
from sqlalchemy import exc
from sqlalchemy import pool as poollib
from sqlalchemy import util
from sqlalchemy.sql import compiler


def create_engine(url, **kwargs):
	
	if "strategy" in kwargs:
		strat = kwargs.pop("strategy")
		if strat == "mock":
			return create_mock_engine(url, **kwargs)
		else:
			raise exc.ArgumentError("unknown strategy: %r" % strat)
	
	kwargs.pop("empty_in_strategy", None)
	
	# create url.URL object
	u = _url.make_url(url)
	
	u, plugins, kwargs = u._instantiate_plugins(kwargs)
	
	entrypoint = u._get_entrypoint()
	dialect_cls = entrypoint.get_dialect_cls(u)
	
	if kwargs.pop("_coerce_config", False):
		
		def pop_kwarg(key, default=None):
			value = kwargs.pop(key, default)
			if key in dialect_cls.engine_config_types:
				value = dialect_cls.engine_config_types[key](value)
			return value
	
	else:
		pop_kwarg = kwargs.pop
	
	dialect_args = {}
	# consume dialect arguments from kwargs
	for k in util.get_cls_kwargs(dialect_cls):
		if k in kwargs:
			dialect_args[k] = pop_kwarg(k)
	
	dbapi = kwargs.pop("module", None)
	if dbapi is None:
		dbapi_args = {}
		for k in util.get_func_kwargs(dialect_cls.dbapi):
			if k in kwargs:
				dbapi_args[k] = pop_kwarg(k)
		dbapi = dialect_cls.dbapi(**dbapi_args)
	
	dialect_args["dbapi"] = dbapi
	
	dialect_args.setdefault("compiler_linting", compiler.NO_LINTING)
	enable_from_linting = kwargs.pop("enable_from_linting", True)
	if enable_from_linting:
		dialect_args["compiler_linting"] ^= compiler.COLLECT_CARTESIAN_PRODUCTS
	
	for plugin in plugins:
		plugin.handle_dialect_kwargs(dialect_cls, dialect_args)
	
	# create dialect
	dialect = dialect_cls(**dialect_args)
	
	# assemble connection arguments
	(cargs, cparams) = dialect.create_connect_args(u)
	cparams.update(pop_kwarg("connect_args", {}))
	cargs = list(cargs)  # allow mutability
	
	# look for existing pool or create
	pool = pop_kwarg("pool", None)
	if pool is None:
		
		def connect(connection_record=None):
			if dialect._has_events:
				for fn in dialect.dispatch.do_connect:
					connection = fn(dialect, connection_record, cargs, cparams)
					if connection is not None:
						return connection
			return dialect.connect(*cargs, **cparams)
		
		creator = pop_kwarg("creator", connect)
		
		poolclass = pop_kwarg("poolclass", None)
		if poolclass is None:
			poolclass = dialect.get_dialect_pool_class(u)
		pool_args = {"dialect": dialect}
		
		# consume pool arguments from kwargs, translating a few of
		# the arguments
		translate = {
			"logging_name": "pool_logging_name",
			"echo": "echo_pool",
			"timeout": "pool_timeout",
			"recycle": "pool_recycle",
			"events": "pool_events",
			"reset_on_return": "pool_reset_on_return",
			"pre_ping": "pool_pre_ping",
			"use_lifo": "pool_use_lifo",
		}
		for k in util.get_cls_kwargs(poolclass):
			tk = translate.get(k, k)
			if tk in kwargs:
				pool_args[k] = pop_kwarg(tk)
		
		for plugin in plugins:
			plugin.handle_pool_kwargs(poolclass, pool_args)
		
		pool = poolclass(creator, **pool_args)
	else:
		if isinstance(pool, poollib.dbapi_proxy._DBProxy):
			pool = pool.get_pool(*cargs, **cparams)
		
		pool._dialect = dialect
	
	# create engine.
	if pop_kwarg("future", False):
		from sqlalchemy import future
		
		# future.Engine对象
		default_engine_class = future.Engine
	else:
		default_engine_class = base.Engine
	
	engineclass = kwargs.pop("_future_engine_class", default_engine_class)
	
	engine_args = {}
	for k in util.get_cls_kwargs(engineclass):
		if k in kwargs:
			engine_args[k] = pop_kwarg(k)
	
	# internal flags used by the test suite for instrumenting / proxying
	# engines with mocks etc.
	_initialize = kwargs.pop("_initialize", True)
	_wrap_do_on_connect = kwargs.pop("_wrap_do_on_connect", None)
	
	# all kwargs should be consumed
	if kwargs:
		raise TypeError(
			"Invalid argument(s) %s sent to create_engine(), "
			"using configuration %s/%s/%s.  Please check that the "
			"keyword arguments are appropriate for this combination "
			"of components."
			% (
				",".join("'%s'" % k for k in kwargs),
				dialect.__class__.__name__,
				pool.__class__.__name__,
				engineclass.__name__,
			)
		)
	
	engine = engineclass(pool, dialect, u, **engine_args)
	
	if _initialize:
		do_on_connect = dialect.on_connect_url(u)
		if do_on_connect:
			if _wrap_do_on_connect:
				do_on_connect = _wrap_do_on_connect(do_on_connect)
			
			def on_connect(dbapi_connection, connection_record):
				do_on_connect(dbapi_connection)
			
			event.listen(pool, "connect", on_connect)
		
		def first_connect(dbapi_connection, connection_record):
			c = base.Connection(
				engine,
				connection=dbapi_connection,
				_has_events=False,
				# reconnecting will be a reentrant condition, so if the
				# connection goes away, Connection is then closed
				_allow_revalidate=False,
			)
			c._execution_options = util.EMPTY_DICT
			
			try:
				dialect.initialize(c)
			finally:
				# note that "invalidated" and "closed" are mutually
				# exclusive in 1.4 Connection.
				if not c.invalidated and not c.closed:
					# transaction is rolled back otherwise, tested by
					# test/dialect/postgresql/test_dialect.py
					# ::MiscBackendTest::test_initial_transaction_state
					dialect.do_rollback(c.connection)
		
		# previously, the "first_connect" event was used here, which was then
		# scaled back if the "on_connect" handler were present.  now,
		# since "on_connect" is virtually always present, just use
		# "connect" event with once_unless_exception in all cases so that
		# the connection event flow is consistent in all cases.
		event.listen(
			pool, "connect", first_connect, _once_unless_exception=True
		)
	
	dialect_cls.engine_created(engine)
	if entrypoint is not dialect_cls:
		entrypoint.engine_created(engine)
	
	for plugin in plugins:
		plugin.engine_created(engine)
	
	return engine


def engine_from_config(configuration, prefix="sqlalchemy.", **kwargs):
    """Create a new Engine instance using a configuration dictionary.

    The dictionary is typically produced from a config file.

    The keys of interest to ``engine_from_config()`` should be prefixed, e.g.
    ``sqlalchemy.url``, ``sqlalchemy.echo``, etc.  The 'prefix' argument
    indicates the prefix to be searched for.  Each matching key (after the
    prefix is stripped) is treated as though it were the corresponding keyword
    argument to a :func:`_sa.create_engine` call.

    The only required key is (assuming the default prefix) ``sqlalchemy.url``,
    which provides the :ref:`database URL <database_urls>`.

    A select set of keyword arguments will be "coerced" to their
    expected type based on string values.    The set of arguments
    is extensible per-dialect using the ``engine_config_types`` accessor.

    :param configuration: A dictionary (typically produced from a config file,
        but this is not a requirement).  Items whose keys start with the value
        of 'prefix' will have that prefix stripped, and will then be passed to
        :func:`_sa.create_engine`.

    :param prefix: Prefix to match and then strip from keys
        in 'configuration'.

    :param kwargs: Each keyword argument to ``engine_from_config()`` itself
        overrides the corresponding item taken from the 'configuration'
        dictionary.  Keyword arguments should *not* be prefixed.

    """

    options = dict(
        (key[len(prefix) :], configuration[key])
        for key in configuration
        if key.startswith(prefix)
    )
    options["_coerce_config"] = True
    options.update(kwargs)
    url = options.pop("url")
    return create_engine(url, **options)