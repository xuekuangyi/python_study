"""
collections是日常工作中的重点、高频模块，常用类型有：
　　计数器（Counter）
　　双向队列（deque）
　　默认字典（defaultdict）
　　有序字典（OrderedDict）
　　可命名元组（namedtuple）

namedtuple是一个 工厂函数，定义在python标准库的collections模块中，使用此函数可以创建一个可读性更强的元组
namedtuple函数所创建（返回）的是一个 元组的子类（python中基本数据类型都是类，且可以在buildins模块中找到）
namedtuple函数所创建元组，中文名称为 具名元组
在使用普通元组的时候，我们只能通过index来访问元组中的某个数据
使用具名元组，我们既可以使用index来访问，也可以使用具名元组中每个字段的名称来访问
值得注意的是，具名元组和普通元组所需要的内存空间相同，所以 不必使用性能来权衡是否使用具名元组

namedtuple是一个函数
namedtuple(typename, field_names, *, rename=False, defaults=None, module=None):
有两个必填参数typename和field_names

typename
参数类型为字符串
具名元组返回一个元组子对象，我们要为这个对象命名，传入typename参数即可

field_names
参数类型为字符串序列
用于为创建的元组的每个元素命名，可以传入像['a', 'b']这样的序列，也可以传入'a b'或'a, b'这种被逗号或空格分割的单字符串
必须是合法的标识符。不能是关键字如class,def等

rename

注意的参数中使用了*，其后的所有参数必须指定关键字
参数为布尔值
默认为False。当我们指定为True时，如果定义field_names参数时，出现非法参数时，会将其替换为位置名称。如['abc', 'def', 'ghi', 'abc']会被替换为['abc', '_1', 'ghi', '_3']

defaults

参数为None或者可迭代对象
当此参数为None时，创建具名元组的实例时，必须要根据field_names传递指定数量的参数
当设置defaults时，我们就为具名元组的元素赋予了默认值，被赋予默认值的元素在实例化的时候可以不传入
当defaults传入的序列长度和field_names不一致时，函数默认会右侧优先
如果field_names是['x', 'y', 'z']，defaults是(1, 2)，那么x是实例化必填参数，y默认为1，z默认为2

"""
from collections import namedtuple
import db_connections

# 通过调用namedtuple('类名',[类属性名1,类属性名2，……类属性名n])方法，
# 返回一个类名为参数中类名的的类，[]中的内容因为是类中的属性名，所以要避免使用关键字，
# Point = namedtuple('Point', ['x', 'y'])
# # 通过构造器来赋值类属性来实例化出对象p，像普通的类一样使用
# p = Point(11, y=22)
# # 像普通的元组一样，使用索引访问
# p[0] + p[1]
# # 像普通的元组一样，解包赋值给变量
# a, b = p
#
# print(b)
# # 像普通对象一样访问属性值
# print(p.y)
# # 调用__repr__方法
# print(p)

# 具名元组在存储csv或者sqlite3返回数据的时候特别有用


PurchaseOrderDetailsRecord = namedtuple('PurchaseOrderDetailsRecord',
                                        ['unique_id', 'belong_to_po', 'details_no', 'po_create_time',
                                         'goods_no', 'quantity', 'purchase_price', 'subtotal',
                                         'data_creator', 'data_create_time', 'data_update_user',
                                         'data_update_time', 'data_update_reason', 'biz_creator',
                                         'biz_create_time', 'post_operator', 'post_time', 'biz_status',
                                         'remarks', 'reserve_columns_01', 'status'])

sql = 'select * from po_details limit 3'


def record(result=db_connections.db_operation(sql)):
	for row in map(PurchaseOrderDetailsRecord._make(), result):
		return row
