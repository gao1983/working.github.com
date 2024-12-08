#五层房子
#每层是10个房间
#数据类型
#循环控制
#循环跳出
for floor in range(1,6):
    if floor == 4:
        print(f'第{floor}层正在装修不对外使用')
        continue
    print(f"欢迎光临吉祥大厦第{floor}层")
    for room in range(1,10):
        if floor == 5 and room == 4:
            print(f'{floor}0{room}已经被总统预定禁止对外')
            continue
        print(f'欢迎进入第{floor}0{room}房间')
