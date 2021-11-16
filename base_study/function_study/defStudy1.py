def function1(return_value):
    test = f'您输入的值为:{return_value}'
    return test


# print(function1(input('请输入>')))
def add_to_list(lv=[]):  # 默认参数应该使用不可变对象
    while True:
        lv.append('END')
        print(lv)
        use_input()
    return lv

def show_tuple(*arg):
    return arg


#
# def add_to_the_end(*par):
#     result = 0
#     j = 0
#     for i in par:
#         result += i
#         j += 1
#     print(result)
#     print(j)
#
#
# # par = input('请输入多个累加数字值之间使用英文逗号分割>>')
# # add_to_the_end(eval(input()))
# par1 = tuple(input('请输入英文逗号分割的多个数值>'))
#
# add_to_the_end(par1)


def add_to_the_end(*par):
    result = 0
    jj = 0
    print(f'par的值为：{par}, par的类型为{type(par)}')
    for ii in par:
        print(f'ii的值为：{ii},ii的类型为{type(ii)}')
        print(f'result类型为：{type(result)}，result的类型为：{type(result)}')
        print(str(jj + 1) * 20)
        result += ii
        jj += 1
    print(f'循环输出结果{result}')
    print(f'循环执行次数{jj}')


def to_put_par(*par0):
    print('第一层参数par0:', type(par0), par0)
    out_par = 0
    tpp_i = 0
    for single in par0:
        print(f'第二层参数single:{type(single), single}')
        for single02 in single:
            # print(type(single02), single02)
            out_par += single02
            tpp_i += 1
            # print(f'tpp_i:{tpp_i}')
            print(f'第三层参数single02:{type(single02), single02}')
    print(f'总计金额{out_par}')
    return out_par


def use_input():
    choice = input(f'请选择需要执行的函数，展示函数清单请输入help>>>')
    while True:
        if choice == 'help':
            print('''
            i —— 累加程序 直接输入input()
            e —— 累加程序 eval(input())
            atl —— add_to_list()
            ''')
            choice = input(f'请选择需要执行的函数，展示函数清单请输入help>>>')

        elif choice == 'i':     # 当输入值为i时，直接使用input
            print('你选择的是input,请继续输入>>>')
            to_put_par(input())
            break
        elif choice == 'e':     # 当输入值为e时，使用eval()方法
            print('你选择的是eval(input()),请继续输入>>>')
            to_put_par(eval(input()))
            break
        elif choice == 'atl':
            print('你选择的是，测试add_to_list(lv=[])>>>,请输入')
            add_to_list(list(input()))
            break
        else:
            print('调用use_input()方法时输入参数错误，请保证只输入help中展示的选项')
            choice = input()


use_input()
