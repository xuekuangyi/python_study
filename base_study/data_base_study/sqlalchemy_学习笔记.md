# ORM与sqlalchemy

**对象关系映射**：Object Relational Mapping

- 将数据库表映射为面向对象程序中的对象，使得在面向对象的程序中，可以更方便纯粹地去操作数据库元素，而不必深陷于去编辑与面向对象语言分割迥异的数据库操作。
- 面向对象是从软件工程基本原则（如耦合、聚合、封装）的基础上发展起来的，而关系数据库则是从数学理论发展而来的，两套理论存在显著的区别。
为了解决这个不匹配的现象，对象关系映射技术应运而生。

SQLAlchemy是用Python编程语言开发的一个开源项目。它提供了SQL工具包和ORM（对象关系映射）工具，使用MIT许可证发行。

SQLAlchemy采用简单的Python语言，提供高效和高性能的数据库访问，实现了完整的企业级持久模型。
它的理念是，SQL数据库的量级和性能比对象集合重要，而对象集合的抽象又重要于表和行。


<div style="font-weight: bolder; font-size: 20px">
一些基础概念：
</div>

- **`ACID 模型`**
“原子性、一致性、隔离性、持久性”的首字母缩写;一组属性，保证数据库事务被可靠地处理。(维基百科)
  - **原子性**是ACID模型的一个组件，它要求每个事务都是“全有或全无”的:如果事务的一部分失败，整个事务就失败，并且数据库状态保持不变。
  原子系统必须保证在每一种情况下都具有原子性，包括电源故障、错误和崩溃。(维基百科)
  - **一致性**是ACID模型的一个组件，它确保任何事务都将数据库从一个有效状态带到另一个有效状态。
  根据所有定义的规则，写入数据库的任何数据必须是有效的，包括但不限于约束、级联、触发器以及它们的任何组合。(维基百科)
  - ACID模型的**隔离属性**确保事务的并发执行会导致系统状态，如果事务是串行执行的，即一个接一个地执行，就会获得这种状态。
  每个事务必须在完全隔离的情况下执行，即如果T1和T2并发执行，则每个事务应保持彼此独立。(维基百科)
  - **持久性**是ACID模型的一个属性，这意味着一旦事务被提交，它将保持原样，即使在电源损耗、崩溃或错误的情况下也是如此。
  例如，在关系数据库中，一旦一组SQL语句执行，结果需要永久存储(即使数据库随后立即崩溃)。(维基百科)
- **注释**是SQLAlchemy内部使用的一种概念，目的是将附加信息与ClauseElement对象一起存储。
Python字典与对象的一个副本相关联，其中包含对各种内部系统都很重要的键/值对，主要在ORM中:
- `**DBAPI**`
DBAPI是短语“Python数据库API规范”的缩写。
    这是Python中广泛使用的规范，用于定义所有数据库连接包的通用使用模式。
    DBAPI是一种“低级”API，通常是Python应用程序中用于与数据库对话的最低级别系统。
    SQLAlchemy的方言系统是围绕DBAPI的操作构建的，它提供独立的方言类，这些方言类在特定的数据库引擎上为特定的DBAPI服务;
    例如，the create_engine() URL postgresql+psycopg2://@localhost/test
    refers to the psycopg2 DBAPI/dialect combination, 
    whereas the URL mysql+mysqldb://@localhost/test refers to the MySQL for Python DBAPI/dialect combination.

关于sqlalchemy
sqlalchemy分为Core部分和ORM部分

<div style="font-size: 20px; font-weight: bolder">
概览
</div>

**什么是SQLAlchemy**?

![img.png](img.png)

SQLAlchemy SQL工具包和对象关系映射器是一组用于处理数据库和Python的综合工具。它有几个不同的功能区域，可以单独使用，也可以组合使用。它的主要组件如下所示，组件依赖关系被组织成层:

>SQLAlchemy有为两个不同的api，后者构建在前者之上。这两个api被称为Core和ORM。
- **SQLAlchemy Core**是SQLAlchemy作为“数据库工具包”的基础架构。
像是pymysql对于mysql,这个库提供了一些工具，用于管理与数据库的连接，与数据库查询和结果交互，以及编程构建SQL语句。
- **SQLAlchemy ORM**构建在Core之上，提供了可选的对象关系映射功能。
ORM提供了一个额外的配置层，允许用户定义的Python类映射到数据库表和其他构造，以及称为Session的对象持久化机制。
然后，它扩展了核心级SQL表达式语言，以允许根据用户定义的对象组合和调用SQL查询。

**版本检查**:

```python
import sqlalchemy
sqlalchemy.__version__
```


<div style="font-size: 20px; font-weight: bolder">
文档内容概要
</div>

- **创建连接**——**引擎**——所有SQLAlchemy应用程序都从**引擎对象**开始;
- **使用事务和DBAPI**——引擎及其相关对象的使用Connection对象返回Result。
这些内容是以SQLAlchemy Core为核心的内容，但学习ORM也至少要了解Result对象。
- **使用数据库元数据**——SQLAlchemy本质是将SQL抽象实现ORM，它依赖于将数据库模式构造定义为Python对象。
需要了解从Core和ORM两个角度如何实现这一点。
- **使用和操作数据**——学习如何在实现数据库的增删改查操作。这里所谓的CRUD操作是以SQLAlchemy Core的形式给出的，并带有指向ORM对应对象的链接。
在用Core或ORM选择行中详细介绍的SELECT操作同样适用于Core和ORM。
- ORM的数据操作涵盖了ORM的持久性框架;基本上是以orm为中心的插入、更新和删除方法，以及如何处理事务。


## 1. 建立连接 - 引擎
任何SQLAlchemy应用程序都是从一个名为Engine的对象开始的，译文：任何SQLAlchemy应用程序的起点都是一个名为Engine的对象。
该对象充当到特定数据库的连接的中心源，为这些数据库连接提供工厂和称为连接池的存储空间。
引擎通常是一个全局对象，只为特定的数据库服务器创建一次，并使用一个URL字符串进行配置，该字符串将描述它应该如何连接到数据库主机或后端。。

**使用`create_engine()`方法创建引擎**
create_engine方法的主要参数是一个字符串URL，这个字符串告诉引擎三个重要的内容:
1. 使用的是哪种数据库?它在SQLAlchemy中链接到一个称为“dialect”的对象。
    - 在SQLAlchemy中，“dialect”是一个Python对象，
  它表示允许数据库操作在特定类型的数据库后端和该数据库的特定类型的Python驱动程序(或DBAPI)上进行的信息和方法。
  SQLAlchemy方言是Dialect类的子类。`class sqlalchemy.engine.Dialect`
2. 使用的是哪种数据库驱动程序？ 
3. 如何定位到数据库？把用户名+密码、地址+端口、数据库名都指定好
**具体形参如下：**
- URL：是第一个形参，通常是指示数据库连接所需的产品、驱动、地址、登录等信息
  - URL的字符串形式为 dialect[+driver]://user:password@host/dbname 
    - `dialect`是数据库名称：例如mysql，oracle，postgresql等；
    - `driver`是驱动名称：driver DBAPI的名称，例如 pymysql、psycopg2、pyodbc、cx_oracl
    - `user`是用户名、`password`密码，@后面跟`地址:端口号`，`dbname`是数据库名
- echo：它将指示Engine将它发出的所有SQL记录到将写入标准输出的Python日志记录器中。
这个标志是一种更正式地设置Python日志记录的简写方法，对于在脚本中进行实验非常有用。
许多SQL示例将在[SQL]链接下面包含SQL日志输出，单击该链接将显示完整的SQL交互。
- future：
```python
import sqlalchemy

# 使用create_engine()方法创建引擎对象
engine = sqlalchemy.create_engine(
	"dialect+driver://username:password@host:port/dbname",
	echo=True, future=True)
```
**延迟连接：**
当第一次调用create_engine()方法返回创建的引擎对象时，实际上还没有尝试连接到数据库;
只有在第一次要求它对数据库执行任务时才会发生这种情况。这是一种被称为初始延迟初始化的软件设计模式。

## 2.使用事务和DBAPI
当Engine对象准备好后，需要进一步操作Engine来实现后续操作数据的要求，其主要交互抓手是Connection和Result。
随后还要将这些对象引入ORM的facade，称为Session。
> 当使用ORM时，引擎由另一个名为Session的对象管理。
> 现代SQLAlchemy中的Session强调事务和SQL执行模式，这与Connection模式基本相同。。

<font style="font-size:20px; font-weight:bold">获得一个连接：</font>

从用户的角度来看，Engine对象的唯一目的是提供一个到数据库的连接单元，称为Connection。
当直接使用Core时，操作Connection对象是完成与数据库所有交互的方式。
由于Connection代表数据库的开放资源，我们希望始终将该对象的使用范围限制在特定的上下文中，
而做到这一点的最佳方法是使用Python上下文管理器表单，也称为with语句。
下面的内容演示了用SQL写就的HelloWorld:

文本SQL是使用一个称为text()的结构发出的:利用名为Connection.execute()的方法，结合名为text()的对象，在数据库上运行SQL语句，并返回一个名为Result的对象。

译文：在使用Session.execute()方法时，本节的大部分内容同样适用于现代ORM使用，它的工作原理与Connection.execute()非常相似，
包括ORM结果行是使用与Core相同的result接口交付的。

```python
import sqlalchemy

# 创建引擎
engine = sqlalchemy.create_engine()

# 利用名为Connection.execute()的方法，结合名为text()的对象，在数据库上运行SQL语句，并返回一个名为Result的对象。
with engine.connect() as conn:
	result = conn.execute(sqlalchemy.text("select * from goods"))
	print(result.all())

```

在上面的示例中，上下文管理器提供了数据库连接，并在事务中构造了操作。
Python DBAPI的默认行为包括事务总是在进行中;当释放连接的范围时，将发出ROLLBACK以结束事务。
事务不是自动提交的;当我们想要提交数据时，我们通常需要调用Connection.commit()方法

<font style="font-size:20px">**提交修改**</font>

DBAPI连接是非自动提交的。如果需要提交一些数据，例如创建一个表并插入一些数据，就需要调用`Connection.commit()`方法
来提交事务，该方法在获取Connection对象的块中调用：

```python
import sqlalchemy

engine = sqlalchemy.create_engine()
# 构建connect对象
with engine.connect() as conn:
	# connect对象的execute方法
	# text方法
	conn.execute(sqlalchemy.text("CREATE TABLE some_table (x int, y int)"))
conn.execute(
	sqlalchemy.text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
	[{"x": 1, "y": 1}, {"x": 2, "y": 4}]
)
# 实际执行过程中发现并不需要commit()了,而且这么写会报错提示，新版本不需要操作提交？
conn.commit()
```

<font style="font-size:20px; font-weight:bold">基础语句执行</font>

**获取行**

```python
import sqlalchemy

engine = sqlalchemy.create_engine()
# 构建connect对象
with engine.connect() as conn:
	result = conn.execute(sqlalchemy.text(
		f'select * from user'
	))

```

```python
import sqlalchemy

def dml_test():
	engine = sqlalchemy.create_engine()
	with engine.connect() as conn:
		result = conn.execute(sqlalchemy.text(
			f"select * from user"))
		
		# 循环可迭代对象result,逐次打印结果
		for row in result:
			print(type(row))    # 打印结果为:<class 'sqlalchemy.engine.row.LegacyRow'>
			print(f"uid:{row.uid} username:{row.user_name}")
```

上面的几个例子中的返回的对象都为Result，它表示**结果行**的可迭代对象。
最后的例子中,使用`print(type(row))`打印出的`<class 'sqlalchemy.engine.row.LegacyRow'>`就可以看得出来.



Result有很多方法用于获取和转换行，例如前面演示的Hello_World中打印时调用的Result.all()方法，
它返回所有Row对象的列表。它还实现了Python迭代器接口，以便我们可以直接遍历Row对象的集合。

Row对象本身的很像是Python中的元组(估计是重写了__str__()方法,所以打印出的结果看起来和元组一样)。
_行有以下的访问方式_:

**元组赋值**——这是最python惯用的风格，它是在每一行被接收时按位置分配变量,很多时候也被称为"拆包"

```python
result =conn.execute(sqlalchemy.text("select c1,c2 from table"))
for x, y in result:
	pass
```
**整数索引**——元组是Python序列，所以常规的整数索引值访问也是可用的:
```python
result = conn.execute(text("select c1, c2 from table"))
  for row in result:
      x = row[0]    # 按索引访问
```

**属性名称**——由于这些是Python命名的元组，元组具有与每一列的名称匹配的动态属性名称。
这些名称通常是SQL语句分配给每行中的列的名称。
虽然它们通常是相当可预测的，也可以通过标签来控制，但在定义较少的情况下，它们可能受制于特定于数据库的行为:
```python
result = conn.execute(text("select * from user"))

for row in result:

    # illustrate use with Python f-strings
    print(f"UID: {row.uid} 名字: {row.user_name}")
```
**映射访问**——使用Python对象接收Row对象映射内容，这本质上是Python对通用dict对象的接口的只读版本，
可以使用Result.mappings()修饰符将Result转换为MappingResult对象;
这是一个结果对象，产生类似于字典的RowMapping对象，而不是Row对象,它是Result的包装器，它返回字典值而不是Row值。
这点和pymysql的pymysql.cursors.DictCursor类似效果;
```python
result = conn.execute(text("select uid, user_name from user"))

# 注意result.mappings()方法,对返回的行应用映射筛选器，返回一个MappingResult实例。
for dict_row in result.mappings():
    uid = dict_row['uid']
    user_name = dict_row['user_name']
```
`method sqlalchemy.engine.Result.mappings()`

<div style="font-size: 20px; font-weight: bold">
	发送参数
</div>
SQL语句通常伴随着与语句本身一起传递的数值内容，前面的实例中的INSERT语句中的字段值;
因此，Connection.execute()方法也接受参数，这些参数被称为<span style="color: red">绑定参数</span>。
例如:如果我们希望将SELECT语句的where子句限制为“y”值大于传递给函数的特定值:
实现方式可以是SQL语句可以保持固定，驱动程序可以正确地清理值，我们在语句中添加了一个WHERE子句，命名一个名为“y”的新参数;
**语法格式:**
text()构造使用冒号格式“`:y`”接受这些值。然后，"`:y `"的实际值**以字典的形式**作为第二个参数
传递给Connection.execute():`{"y": 2}`

```python
with engine.connect() as conn:
     result = conn.execute(
	     # 可以不必再像原生的python一样用f字符中写法了f"select * from table where y>{y}}"
         text("SELECT x, y FROM some_table WHERE y > :y"),
         {"y": 2}
     )
     for row in result:
        print(f"x: {row.x}  y: {row.y}")
```
**多个参数绑定**
使用英文逗号分割"变量"和"键值对"

```python
with engine.connect() as conn:
     conn.execute(
         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
         [{"x": 11, "y": 12}, {"x": 13, "y": 14}]
     )
     conn.commit()
```

<div style="color: #66afe9">
虽然上面举例都是用的SQL脚本的方式,但在使用了sqlalchemy框架后,基本不会去写脚本的方式,一是这与ORM存在的意义相悖,
而且还会有安全问题,如著名的SQL注入,所以当使用SQL时，Python文字值，等非字符串数据类型的数据,如整数或日期，
也不应该直接字符串化为SQL字符串;应该始终使用参数。
然而，它也允许SQLAlchemy方言和/或DBAPI正确地处理后端输入。
在纯文本SQL用例之外，SQLAlchemy的核心表达式API确保在适当的情况下将Python文字值作为绑定参数传递。
</div>

<span style="font-size: 20px; font-weight: bold">
将参数与语句绑定:
</span>

前面两种情况说明了与SQL语句一起传递的一系列参数。
对于单个参数声明执行SQLAlchemy使用参数实际上是往往通过捆绑与语句本身的参数,
这是一个SQL表达式语言的主要功能,使查询,可以由自然同时利用参数化在所有情况下。
这个概念将在接下来的章节中进行更详细的讨论;简单地看一下，text()构造本身是SQL表达式语言的一部分

```python
stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
with engine.connect() as conn:
	result = conn.execute(stmt)
    for row in result:
        print(f"x: {row.x}  y: {row.y}")
```
值得注意的是，尽管我们只向Connection.execute()方法传递了一个参数stmt，但语句的执行说明了SQL字符串和单独的参数元组。

<div style="font-size: 20px; font-weight: bolder">
使用ORM session执行
</div>
上面Core方式实现的大多数模式和示例也适用于ORM,下面结合Core和ORM的使用来说明每种模式。
使用ORM时，基本的事务/数据库交互对象称为Session。
在现代SQLAlchemy中，这个对象的使用方式与Connection非常相似，事实上，在使用Session时，它在内部引用一个Connection，它使用这个Connection发出SQL。

当将Session与非orm结构一起使用时，它执行SQL的方式和Connection直接执行的操作没有太大区别
下面的例子可以比作捆绑的前一节中的示例参数直接与声明,只不过是将调用engine.connect()获得返顺的conn,
换成了调用session()获得返回的session,与康涅狄格州会话(引擎)会话,然后再调Session.execute()方法,
就像前面调用Connection.execute()方法一样。

```python
from sqlalchemy.orm import Session

stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
with Session(engine) as session:
     result = session.execute(stmt)
     for row in result:
        print(f"x: {row.x}  y: {row.y}")

```

同样的,和Connection一样，Session的特点是使用Session.commit()方法来实现“commit as you go”

```python
with Session(engine) as session:
...     result = session.execute(
...         text("UPDATE some_table SET y=:y WHERE x=:x"),
...         [{"x": 9, "y":11}, {"x": 13, "y": 15}]
...     )
...     session.commit()
```
注:在结束事务之后，Session实际上并不持有Connection对象。当下一次需要对数据库执行SQL时，它从引擎获得一个新的Connection。

Session有几个不同的创建模式:



