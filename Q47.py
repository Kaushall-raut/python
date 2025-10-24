total_bonus = 0  # To store total bonus paid by the company

for i in range(5):
    print(f"\nEmployee {i+1}:")
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    experience = int(input("Enter experience (years): "))


    if experience >= 10:
        bonus = salary * 0.10
    elif experience >= 5:
        bonus = salary * 0.05
    else:
        bonus = 0

    total_bonus += bonus  
    print(f"{name} will receive a bonus of: {bonus}")

print(f"\nTotal bonus paid by the company: {total_bonus}")
