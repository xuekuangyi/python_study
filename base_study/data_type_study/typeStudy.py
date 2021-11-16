# 整型、浮点型基本代数运算
import builtins

print(1 + 3)  # 整型加法
print(5 - 2)  # 整型减法
print(5 * 8)  # 整型除法
print(9 // 3)  # 除法得整型结果
print(10 // 3)  # 除法得整型结果
print(9 / 3)  # 除法得浮点型结果
print(10 / 3)  # 除法得浮点型结果

print(type(10 // 3))  # 整型结果
print(type(9 / 3))  # 浮点型结果

print(10 % 3)  # 取余
print(2 ** 3)  # 乘方运算a^b

x = 3
x = x + 1
print(x)
y = 5
y += 2  # y = y+2
print(y)
z = 9
z -= 3  # z = z-3
print(z)

print('4.44修约', round(4.44), ',4.54修约', round(4.54), ',4.55修约', round(4.55))

import math

print('4.53四舍五入得', math.ceil(4.53))
print('5.9向下取整得', math.floor(5.9))
print('5.1向上取整得', math.ceil(5.1))

# 字符串类型
print('a' + 'B')
# 布尔类型
print(type(True))

# 元组类型
tuple_type = (1, 2, 3, 4, 5)  # 元组内容不可改；
list_type = [1, 2, 3, 4, 5]
set_type = {1, 2, 3, 4, 5}

print(type(tuple_type), tuple_type, '[1:3]:', tuple_type[1:3])
builtins.print(type(list_type), list_type, '[1:3]:',list_type[1:3])
print(type(set_type), set_type, '[1:3]:', list_type[1:3])
print(type(set_type), set_type, '[1:]:', list_type[1:])
print(type(set_type), set_type, '[:3]:', list_type[:3])
print(type(set_type), set_type, '[:-1]:', list_type[:-1])
print(type(set_type), set_type, '[2]:', list_type[2])

# print(set_type[1:2])