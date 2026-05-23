from menu import show_menu
from actions import add_students, show_students, show_top_students, show_general_average, delete_student, show_failed_students
from data import export_students_to_csv, import_students_from_csv

def main():
    print("Welcome to the Student Control System")

    students = []

    while True:
        show_menu()
        option = input("Enter an option number: ")

        if option == "1":
            add_students(students)

        elif option == "2":
           show_students(students)

        elif option == "3":
            show_top_students(students)

        elif option == "4":
            show_general_average(students)

        elif option == "5":
            export_students_to_csv(students)

        elif option == "6":
            import_students_from_csv(students)

        elif option == "7":
            delete_student(students)

        elif option == "8":
            show_failed_students(students)
        
        elif option == "9":
            print("Exiting the students control system. Bye")
            break

        else:
            print("Invalid option: Choose the number between 1 and 9")


if __name__ == "__main__":
    main()