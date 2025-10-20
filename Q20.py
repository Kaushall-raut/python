num=int(input("Enter a number:"))

# store=1
# while num>1:
#     store*=num

#     num-=1
# print(f"factorial of given number is : ",store)

# store=1
# for i in range(num,0,-1):
#     store=store*i

# print(store)


def fact(n):
    
    if(n==1):
        return 1
    return n*fact(n-1)




print(fact(4))