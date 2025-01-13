students = []
names = set()

def showMenu():
    option = 0
    while option != 4:
        print("-" * 20)
        print("1. Add a Student")
        print("2. View all students")
        print("3. Find students older than a specific age")
        print("4. Exit")
        print("-" * 20)
        while True:
            try:
                option = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Please enter a valid number.")
                continue
        if option == 1:
            addStudent()
        elif option == 2:
            viewStudents()
        elif option == 3:
            findStudent()
        elif option == 4:
            print("Exiting the program")
        else:
            print("Invalid option")

def addStudent():
    while True:
            try:
                name = str(input("Enter the student's name: "))
                if not name.isalpha():
                    print("Please enter a valid name.")
                    continue
                if name in names:
                    print("This name already exists.")
                    continue
                age = int(input("Enter the student's age: "))
                students.append((name, age))
                names.add(name)
                print(f"{name}, {age} years old, was successfully added!")
                break
            except ValueError:
                print("Please enter a valid age.")
                continue

def viewStudents():
    if students:
        print("Students:")
        for student in students:
            print(f"- {student[0]}, {student[1]} years old")
    else:
        print("The list is empty.")

def findStudent():

    while True:
        try:
            age = int(input("Enter the age: "))
            break
        except ValueError:
            print("Please enter a valid age.")
            continue
    olderStudents = [student for student in students if student[1] >= age]
    if olderStudents:
        print(f"Students older than {age}:")
        for student in olderStudents:
            print(f"- {student[0]}, {student[1]} years old")
    else:
        print("No students older than the specified age.")

if __name__ == "__main__":
    showMenu()