amount=int(input("Enter an amount"))

if(amount >= 5000):
    store= (amount /100)*20
    print(f"Your final bill is {store}")
elif(amount >= 2000 and amount <5000):
    store= (amount /100)*10
    print(f"Your final bill is {store}")
if(amount < 2000):

    print(f"Your final bill is {amount}")
