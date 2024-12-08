from operator import truediv

age = 25
while True:
    gage = int(input(f"黑姑娘的年龄："))
    if gage <= 10 or gage < 25:
        print("猜小了，往大了猜")
    elif gage > 25 and gage < 30:
        print("猜的太大了，往小了猜")
    elif gage == age:
        print("恭喜你猜对了")
        break
    else:
        print("瞎猜，滚犊子")


