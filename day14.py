import json
try:
    with open("students.json", "r") as file:
        data = json.load(file)

    for student in data:
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
except json.FileNotFoundError:
        print("File not found. Please check the file path and try again.")
except json.JSONDecodeError:
        print("Error decoding JSON. Please check the file content.")
except Exception as e:  
    print("An error occurred:", str(e))



import json
try:
    with open("students.json", "r") as file:
        data = json.load(file)

    for student in data:
        if not isinstance(student["marks"], (int, float)):
            raise ValueError(f"invalid marks format for {student['name']}. Expected a number.")
        {student["name"]}
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
except ValueError as ve:
        print("Value Error:", str(ve))
except json.JSONDecodeError:
        print("Error decoding JSON. Please check the file content.")
except Exception as e:  
    print("An error occurred:", str(e))
