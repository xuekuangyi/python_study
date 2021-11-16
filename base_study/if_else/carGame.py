car_status = '熄火'
command =''     # 变量初始化，不初始化循环首次的判断就会提示无此变量
while True:
#while not(command == '退出' and car_status == '熄火'):  # 可以直接上while True 然后完全交给循环内的if语句+break来去控制，更为顺畅；
    command = input(f'{car_status}>')   # 循环的“根”下使用input()方法中断，只要不出循环，每次循环一次，都回到循环体开头该中断，等待输入
    if command == '帮助':
        print('''启动 - 启动车辆
        熄火 - 车辆熄火
        退出 - 结束游戏
        帮助 - 查看游戏指令''')
    elif car_status == '熄火' and command == '启动':
        print('''车辆启动中……
        车辆启动成功''')
        car_status = '启动'

    elif car_status == '启动' and command == '熄火':
        print('''车辆熄火中……
        熄火成功''')
        car_status = '熄火'
    elif car_status == '熄火' and command == '退出':
        break

    elif car_status == '启动' and command == '启动':
        print('车辆已启动，无需再次启动')
    elif car_status == '启动' and command == '退出':
        print('请先将车辆熄火才可结束游戏')
    elif car_status == '熄火' and command == '熄火':
        print('车辆已熄火，无需再次熄火')

    else:
        print('无法识别的指令')

else:
    print('游戏结束')
    # if command == '关闭':
    #     break


# while 2 > 1:
#     print(not(command == '退出' and car_status == '启动'))
#     print((command == '退出' and car_status == '启动'))
#     print(command == '退出')
#     print(car_status == '启动')
#     command = input(f'{car_status}>')
