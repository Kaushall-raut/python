data = [(2, 4), (1, 1), (4, 2), (4, 3)]


size=len(data)

for i in range(size):
    for j in range(0,size-i-1):
        if data[j][1]>data[j+1][1]:
            data[j],data[j+1]=data[j+1],data[j]

print(data)