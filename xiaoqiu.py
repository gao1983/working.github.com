height = 100
distance = 0
count =0
while count < 10:
    distance += height
    height = height/2
    distance += height
    count += 1
    print(count,distance,height)

n=1
day=11
while day >1:
    n = (n+1)*2
    day -=1
    print(n,day)