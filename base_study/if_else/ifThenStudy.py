# is_true = True
# var1 = 5
# if is_true:
#     print('\t结果为真')
#     print('\t条件为真的第二行语句')
#     if var1 == 10:
#         print('\t\t条件为真且变量等于10')
#     else:
#         print('\t\t条件为真但变更不等于10')
# else:
#     print('\t条件为假')
#     print('\t条件为假的第二条语句')
#
# print('最外层语句')     # 只有当条件为假时才会只输出本条语句，条件为真时，两条语句都执行

x = 30
y = 30
z = 40
if x > y:
    print('第一种情况：x>y')
elif x < y:
    print('第二种情况：x<y')
elif z == x:
    print('第四种情况截胡：z == x')
elif z != x and not x != y:     # 与非
    print('第五种情况截胡：x == y 且z != x')
else:
    print('第三种情况：x == y')


# 逻辑运算符
# AND:  both
# OR:   at least
# NOT:  negate
# and not 同时使用

