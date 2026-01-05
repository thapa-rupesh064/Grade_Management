
def add_student_grade(names, grades, name, grade):
    index = names.index(name) if name in names else 1
    if index != 1:
        grades[index].append(grade)
    else:
        with open("grades.txt", "w" ) as f:
            f.write(name)
            f.write(" : ")
            f.write(f"[{grade}]")

        # names.append(name)
        # grades.append([grade])
def view_all_student_grades(names, grades):
    # if not names:
    #     print("No student grades entered yet.")
    # else:
        # print("All student grades: ")
        # for i in range(len(names)):
        #     print(f"{names[i]}: {grades[i]}")
        with open("grades.txt") as f:
            f.read()
def compute_average_grade(names, grades):
    if not names:
        print("No student grades entered yet.")
    else:
        for i in range(len(names)):
            average_grade = sum(grades[i]) / len(grades[i])
            print(f"Average grade for {names[i]}: {average_grade}")

def main():
    student_names = []
    student_grades = []

    while True:
        print("\nMenu:")
        print("1. Add Student Grade")
        print("2. View All Student Grades")
        print("3. Compute Average Grade for Each Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter student's name: ")
            grade = input("Enter grade for the student: ")
            add_student_grade(student_names, student_grades, name, grade)
            print("Grade added successfully.")

        elif choice == '2':
            view_all_student_grades(student_names, student_grades)

        elif choice == '3':
            print("\nAverage Grades:")
            compute_average_grade(student_names, student_grades)

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
