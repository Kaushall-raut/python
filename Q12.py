m1=int(input("Enter first subject marks"))
m2=int(input("Enter second subject marks"))
m3=int(input("Enter third subject marks"))
m4=int(input("Enter fourth subject marks"))
m5=int(input("Enter fifth subject marks"))



if(m1>100 and m2>100 and m3>100 and m4>100 and m5>100  ):

    print("plz enter the marks under 100")
else :

    total =m1+m2+m3+m4+m5
    if(total>=33):
     print("you passed in all subjects")
    else :
     print("You failed")

