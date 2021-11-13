"""
N个元素的元组或序列，分解成为N个单独的变量——解包
"""

# 任何的序列或是可迭代的对象，都可以通过一个简单的多变量赋值操作来分解到各变量中，唯一的要求就是变量总数和结构要与序列内含元素吻合；
# 元组：
p = (1, 2, 3)
x, y, z = p
# print(f'{type(p)}:\n{x}{y}{z}')

# list
data = ['Jeremy', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(date)
# 元组元素对元组里的变量赋值
name, shares, price, (year, mon, day) = data
print(year)

# 除了元组和列表，只要对象是可迭代的，就可以执行分解操作——字符串、文件、迭代器和生成器：
s = 'Hello'
a, b, c, d, e = s
print(c)


