i = 'y'
while i == 'y':
    power = float(input('请输入功率值'))
    unit = input('请输入功率的单位：马力（ps）还是千瓦（kw）?')
    power_to_change = 0    # 变量初始化
    if unit.upper() == "PS":
        power_to_change = power / 0.7354987  # 当输入的功率值以马力计时，需除以转换系数0.7354987得到对应的以千瓦计的功率值
        print('输入的是马力')
    elif unit.lower() == "kw":
        power_to_change = power * 0.7354987  # 当输入功率值以千瓦计昌，需乘以转换系数0.7354987得到对应的以马力计的功率值
    else:
        print("")
    # print(unit)
    print(f"您输入的功率为{power}{unit.replace('ps', '马力').replace('kw', '千瓦')},换算为{power_to_change}{unit.replace('ps', '千瓦').replace('kw', '马力')}")
    # 请输入正确的功率单位：ps或kw，大小写即可，其它的字母组合为不正确输入
    i = input('是否继续y/n？' )
print('程序结束')