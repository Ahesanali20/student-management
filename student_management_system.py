file_path = "Student Management/Student_Data.txt"

# Load existing data
try:
    with open(file_path, "r") as file:
        student = {}
        for line in file:
            name, marks = line.strip().split(',')
            student[name] = int(marks)
except FileNotFoundError:
    student = {}

while True:
    print("\n------ Student Management App ------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Student Results")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add Student
    if choice == '1':
        name = input("Enter student name: ")
        try:
            marks = int(input("Enter student marks: "))
            student[name] = marks
            # Save data to file
            with open(file_path, "w") as file:
                for name, marks in student.items():
                    file.write(f"{name},{marks}\n")
            print(f"Student '{name}' added successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid number for marks.")

    # View Students
    elif choice == '2':
        if not student:
            print("No students found.")
        else:
            print("\n------ Student List ------")
            for name,marks in student.items():
                print(f"Name: {name}, Marks: {marks}")

    # Check Student Results
    elif choice == '3':
        name = input("Enter student name to check results: ")

        if name in student:
            marks = student[name]

            if marks >= 40:
                print(f"Student '{name}' has passed with {marks} marks.")
            else:
                print(f"Student '{name}' has failed with {marks} marks.")
        else:
            print("Student not found.")

    # Exit
    elif choice == '4':
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")