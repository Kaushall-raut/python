dict1 = {'1': 10, '2': 5, '3': 7}
dict2 = {'1': 3, '3': 2, '4': 8}
dict3={}

for key,value in dict1.items():
   if key in dict2:
        dict3[key]=value + dict2[key]
   else:
       dict3[key]=value


for key, value in dict2.items():
        if key not in dict3:
            dict3[key] = value

print(dict3)