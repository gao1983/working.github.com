
import random

# 员工名单（假设员工是1到300）
employees = [f"员工{str(i)}" for i in range(1, 301)]

# 奖品
first_prize = "iPhone 16"
second_prize = "Apple Pad"
third_prize = "无线耳机"

# 抽奖人数
first_prize_winners = random.sample(employees, 3)
second_prize_winners = random.sample([e for e in employees if e not in first_prize_winners], 10)
third_prize_winners = random.sample([e for e in employees if e not in first_prize_winners and e not in second_prize_winners], 30)

# 打印结果
print("一等奖 (iPhone 16):")
for winner in first_prize_winners:
    print(winner)

print("\n二等奖 (Apple Pad):")
for winner in second_prize_winners:
    print(winner)

print("\n三等奖 (无线耳机):")
for winner in third_prize_winners:
    print(winner)
