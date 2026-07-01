# import json
# with open("students.json", "r") as file:
#     data = json.load(file)

# for student in data:
#     print("ID:", student["id"])
#     print("Name:", student["name"])
#     print("Marks:", student["marks"])
#     print("-------------------")


import json

class Student:
    def __init__(self, id, name, marks):
        self.id = id
        self.name= name
        self.marks = marks
students = [
    Student(101, "Varun", 95),
    Student(102, "Rahul", 88),
    Student(103, "Ammu", 91)
]
student_list = []
for student in students:
    student_list.append(student.__dict__)
with open("students.json", "w") as file:
    json.dump(student_list, file, indent=4)
    print("Student data saved successfully.")
with open("students.json", "r") as file:
    data = json.load(file)
for student in data:
    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print("-------------------")

