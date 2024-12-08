names_list = [ '高嘉鑫','高锦奕','高佳桐','高佳阳' ]
#names[16:26]
for name in names_list:
    print(f" i miss you {name} 好好学习天天向上")

app=names_list.index('高佳桐')
print("显示当前位置",app)
names_list.append('高爷爷')
print(names_list)
names_list.insert(-2,'高狗狗')
print(names_list)
del names_list[2]
print(names_list)
names_list.insert(2,'高佳桐')
print(names_list)
names1_list =['gaoqin','hhh','eee','aa']
print(names1_list[2])
names1_list.append(['gaohong',168,43,23])
print(names1_list)
print(names1_list[-1][2])