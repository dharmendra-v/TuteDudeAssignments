marks = {
    'Alice': 50,
    'Mary': 55,
    'Dylan': 65
}

name = input("Enter the student's name: ")
if name in marks:
    print(f"{name}'s marks: {marks[name]}")
else:
    print("Student not found.")
