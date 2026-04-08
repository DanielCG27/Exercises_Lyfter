# Primera función, pedirle al usuario ingresar un número
def get_number(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError as ex:
            print("Invalid value: ", ex)


def show_menu():
    print("\n1. Sum")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Division")
    print("5. Clear result")
    print("6. Exit")


def calculator():
    first_number = get_number("Enter your number ")
    while True:
        show_menu()
        option = input("Choose the option: ")

        if option == "1":
            new_number = get_number("Add the other number ")
            first_number += new_number
            print("The result is: ", first_number)
        
        elif option == "2":
            new_number = get_number("Add the other number ")
            first_number -= new_number
            print("The result is: ", first_number)
        
        elif option == "3":
            new_number = get_number("Add the other number ")
            first_number *= new_number
            print("The result is: ", first_number)
        
        elif option == "4":
            new_number = get_number("Add the other number ")
            try:
                first_number /= new_number
                print("The result is: ", first_number)
            except ZeroDivisionError as ex:
                print("The division can´t be 0: ", ex)
        
        elif option == "5":
            first_number = 0
            print("The result has been clear: ", first_number)
        
        elif option == "6":
            print("Finish")
            break

        else:
            print("Invalid option")


calculator()