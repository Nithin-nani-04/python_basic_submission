students={
    'nani':85,
    "nithin":95,
    "Alice":85,
}

name = input("Enter the student's name: ")
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("student not found")