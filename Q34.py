num=[2,6,3,2,31,22]

new_list=[]


for i in num:
    if i not in new_list:
        new_list.append(i)


print(new_list)