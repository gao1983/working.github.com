name1_set = {'牛肉','猪肉','羊肉','鸡肉','海鲜','蔬菜'}
name2_set = {'羊肉','猪肉','水果','干果','家具','汽车'}
name3_list = ['牛肉','猪肉','羊肉','鸡肉','海鲜','蔬菜']
print(name1_set.difference(name2_set))
print(name1_set|name2_set)
print(name1_set.intersection(name2_set))
print(name3_list)
print(name3_list.index('羊肉'))
name3_list.append('香蕉')
print(name3_list)