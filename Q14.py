salary=int(input("Enter your annual salary"))


if(salary>250000 and salary <500000 ):
    cal= (salary/100)*5
    print(f"Your Tax is {cal}")
elif(salary>500000 and salary <1000000 ):
    cal= (salary/100)*20
    print(f"Your Tax is {cal}")
elif(salary>1000000):
     cal= (salary/100)*30
     print(f"Your Tax is {cal}")
else:
    print(f"Your Tax is {salary}")