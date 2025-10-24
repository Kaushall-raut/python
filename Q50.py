marks = (80, 65, 90, 55, 77, 88, 45, 92, 70, 60)

highest = max(marks)
lowest = min(marks)

average = sum(marks) / len(marks)

count_75_or_more = 0
for mark in marks:
    if mark >= 75:
        count_75_or_more += 1

print(f"Highest marks: {highest}")
print(f"Lowest marks: {lowest}")
print(f"Average marks: {average}")
print(f"Number of students scoring ≥ 75: {count_75_or_more}")
