height = 100
distance = 0
count =0
while count < 10:
    distance += height
    height = height/2
    distance += height
    count += 1
    print(count,distance,height)