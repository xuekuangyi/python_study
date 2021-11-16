# 例题2
# for item in '12345':
#     print(item)
# print('-' * 10)
# for item2 in [1, 2, 3, 4, 5]:
#     print(item2)

# 例题2
# for x in range(4):
#     print('-' * 10)
#     for y in range(4):
#         print(f'({x},{y})')
# print('-'*10)

# numbers = [5, 2, 5, 2, 2]
# i = 0
# j = 0
#
# for x_count in numbers:  # 循环将数组内容逐个赋值给x_count
#     # print(x_count)
#     i += 1
#     output = ''  # 每次都将output变量“清空”，重置为空字符串
#     for count in range(x_count):  # 使用range()直接指定循环的次数，
#         output = output + 'f'  # 该表达式的意思是循环拼接字段串
#         j = j + 1
#     print(output)  # 循环跳出时，j也被按目标赋值了，打印出来
# print("-" * 10)
# print(f'外层循环执行了 {i}次,内层循环执行了 {j} 次')


# for x_count in '5':
#     output = ''
#     for count in range(x_count):
#         output = output + '1'
#     print(output)

