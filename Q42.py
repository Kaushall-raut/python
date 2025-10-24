from collections import Counter

fruit={1:[1,2,1,2,5],
       2:[2,2,2,4,2],
       3:[4,2,1,2,3]
       }

list=[1,2,1,1,2,3,4,3,2]

print(Counter(list))

for i,j in fruit.items():
    print(f"key :{i}",Counter(j))