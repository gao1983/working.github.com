
li= ['1','2','3','4','1','2','3','4','5','6','7','8','9']
duplicate_num = []
for i in li:
     i_show_count = li.count(i)
     if i_show_count > 1 and [i,i_show_count] not in duplicate_num:
        duplicate_num.append([i, i_show_count])
print(duplicate_num)
for itme in duplicate_num:
    duplicate_n = itme[0]
    duplicate_times = itme[1]
    for j in range (duplicate_times-1):
        li.remove(duplicate_n)
        print(f"删除最近一次",{duplicate_n})

print(li)