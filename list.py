names_list = [ '嘉鑫','锦奕','佳桐','佳阳' ]
#names[16:26]
for name in names_list:
    print(f" i miss you {name} 好好学习天天向上")

app=names_list.index('佳桐')
print("显示当前位置",app)
names_list.append('爷爷')
print(names_list)
names_list.insert(-2,'狗狗')
print(names_list)
del names_list[2]
print(names_list)
names_list.insert(2,'佳桐')
print(names_list)
names1_list =['gaoqin','hhh','eee','aa']
print(names1_list[2])
names1_list.append(['gaohong',168,43,23])
print(names1_list)
print(names1_list[-1][2])