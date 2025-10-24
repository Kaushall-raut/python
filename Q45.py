library = {
    "Python Basics": 4,
    "Data Science": 7,
    "Algorithms": 3,
    "Machine Learning": 10
}

max_copies = -1
max_book = ""

for book, copies in library.items():
    if copies > max_copies:
        max_copies = copies
        max_book = book

print(f"The book with maximum copies is '{max_book}' with {max_copies} copies.")