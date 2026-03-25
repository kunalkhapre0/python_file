# Initialisting dictonary
student_grades = {}


# add a new student
def add_student(names, grade):
    student_grades[names] = grade
    # [ankit] = 100
    print(f"Added{name} with a {grade}")
    # Added ankit with a 00


# Update a student
def update_student(name, grade):
    if name in stuent_grades:
        student_grades[name] = grade
        # ankit = 200
        print(f"{nmae} with marks are update {grade}")

    else:
        print(f"{name} is not found!")


# delate a student
def delate_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been succesfully delated")

    else:
        print(f"{name} is not found!")


# view all student
def dispplay_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")

    else:
        print("No stuedents found added")


def main():
    while True:
        print('\n student Grades Managment System')
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delate Student")
        print("4. view Student")
        print("5. Exit")

        choice = int(input("Enter your choice = "))
        if choice == 1:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name")
            grade = int(input("Enter student grade = "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name")
            grade = int(input("Enter student grade = "))
            delate_student(name, grade)

        elif choice == 4:
            desplay_all_students()

        elif choice == 5:
            print("Closing the program...")
            break

        else:
            print("Invalied choice")
