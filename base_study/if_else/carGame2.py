car_status = 'stopped'  # started/stopped
command = ''     # 变量初始化，不初始化循环首次的判断就会提示无此变量
while True:
    command = input(f'{car_status}>')
    if command == 'start':
        if car_status == 'stopped':
            print('car started success')
            car_status = 'started'
        else:
            print('car has already started')
    elif command == 'stop':
        if car_status != 'stopped':
            print('car stopped success')
            car_status = 'stopped'
        else:
            print('car has already stopped')
    elif command == 'quit':
        if car_status != 'started':
            print('exit the game sucess')
            break
        else:
            print('you must to stop the car first')
    else:
        print('unknown command')
