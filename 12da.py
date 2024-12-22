base =100000
jin = 0.035
year =0
while base <= 200000:
    year +=1
    base += base*jin
    print(year,base)
