number = 5
count = 0
limit_times = 4
print(f'竞猜的总计次数为{limit_times}，输入0退出竞猜')
while count < limit_times:
    count += 1
    if count == 1:
        guess = int(input('请输入猜测的数字'))
    else:
        guess = int(input('是否还要继续竞猜？如果继续请直接输入猜测的数字，否则输入0'))

    if guess == 0:
        print(f'您总计参加{count - 1}次后退出竞猜')
        break
    elif guess == number:
        print(f'恭喜你经过{count}次终于猜中了')
        break
    elif guess != number and count == limit_times - 1:
        print('仅剩一次机会')
    # elif guess != number and count == limit_times:
    #     print(f'{limit_times}次次数全部用完，未猜中')    # 方案2，在if里写条件
    else:
        print(f'机会还剩{limit_times - count}次')
else:
    # guess != number and count == limit_times:
        print(f'{limit_times}次次数全部用完，未猜中')      # 方案1 在循环外写条件