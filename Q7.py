first = int(input("Enter your first subject marks"))
second = int(input("Enter your second subject marks"))
third = int(input("Enter your third subject marks"))


marks = ((first+second+third)/300) * 100
print(marks)
if (marks>=90):
    print("You got an A grade")
elif (marks>=75 and marks <90):
    print("You got an B grade")
elif (marks>50 and marks <75):
    print("You got an c grade")
else:
    print("You Failed")