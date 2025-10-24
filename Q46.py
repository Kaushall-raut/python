salaries = {
    "aa": 48000,
    "ab": 52000,
    "ac": 60000,
    "ad": 45000
}

for employee, salary in salaries.items():
    if salary > 50000:
        print(f"{employee} earns {salary}")
