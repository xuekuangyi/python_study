def add0(*numbers):
    print(type(numbers), numbers)
    sum = 0
    for i in numbers:
        print(type(i), i)
        sum += int(i)
        print(type(sum), sum)
    print('numbers:', numbers)
    print(sum)
    return sum


# add0(input())
# <class 'tuple'> ('1,2,3,4',)
# <class 'str'> 1,2,3,4

def add1(*numbers):
    print(type(numbers), numbers)
    sum = 0
    for i in numbers:
        print(type(i), i)
        sum += int(i)
        print(type(sum), sum)
    print('numbers:', numbers)
    print(sum)
    return sum


# add1(eval(input()))
# 输入结果
# <class 'tuple'> ((1, 2, 3, 4),)
# <class 'tuple'> (1, 2, 3, 4)


def add11(*numbers):
    print('方法名：add11')
    print(f'入参类型及值：{type(numbers), numbers}')
    sum = 0
    for i in numbers:
        print(f'第一层for循环被赋值的类型及值：{type(i), i}')
        for j in i:
            sum += j
            print(f'内层参与运算的变量j的格式及本次值：{type(j), j}')
    print(f'累加总和变量sum的格式及值:{type(sum), sum}')
    return sum


add11(eval(input()))


def add2(*numbers):
    print(type(numbers), numbers)
    sum = 0
    for i in numbers:
        print(type(i), i)
        sum += int(i)
        print(type(sum), sum)
    print('numbers:', numbers)
    print(sum)
    return sum


# add2(tuple(input()))
# <class 'tuple'> (('1', ',', '2', ',', '3', ',', '4'),)
# <class 'tuple'> ('1', ',', '2', ',', '3', ',', '4')


def add3(*numbers):
    print(type(numbers), numbers)
    sum = 0
    for i in numbers:
        print(type(i), i)
        sum += int(i)
        print(type(sum), sum)
    print('numbers:', numbers)
    print(sum)
    return sum


# add3(*(input().split(',')))

def add4(numbers):
    print(type(numbers), numbers)
    sum = 0
    for i in numbers:
        print(type(i), i)
        sum += int(i)
        print(type(sum), sum)
    print('numbers:', numbers)
    print(sum)
    return sum

# add2(input().split(','))


# var1 = '3'
# var2 = 4
# print(f'var1的类型为:{type(var1)},var2的类型为{type(var2)}')
# print(int(var1) + var2)

# 测试更新2:59