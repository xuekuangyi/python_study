# 字符串和元组是不可变的，而列表是可变（mutable）的，可以对它进行随意修改。
# 我们还可以将字符串和元组转换成一个列表，只需使用 list 函数

# 初始化变量
def func1():
    str_study = 'hello'
    tuple_type = ('a', 'b', 'c', 'd')
    list_type = list(str_study)
    print(list_type)
    print(type(list(str_study)), str_study, type(list_type), list_type)  # list()方法可以将字符串转为列表
    print(tuple_type, '>>>', list(tuple_type))  # list()方法可以将元组转为列表


# 常用方法：
# index 方法用于从列表中找出某个元素的位置，如果有多个相同的元素，则返回第一个元素的位置
def func_list():
    var_list = [1, 2, 3, 4, 5, 5, 7, 8]
    element_looking_for = 5
    print(f'元素5在list{elementLookingFor}中出现的位置是:' + str(var_list.index(elementLookingFor) + 1))  # 返回索引位置编号，从0开始

# count 方法用于统计某个元素在列表中出现的次数。

numbers = [1, 2, 3, 4, 5, 5, 7, 8]
counter = 5
print(f'元素{counter}在{numbers}共有', numbers.count(counter))  # 对元素出现此次数记数
print(type(numbers.count(counter)))  # 查看返回的类型是否为int

# 调用函数：
