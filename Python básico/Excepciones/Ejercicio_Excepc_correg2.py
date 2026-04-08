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


def sum(current, new):
    return current + new


def subtract(current, new):
    return current - new


def multiplication(current, new):
    return current * new


def division(current, new):
    return current / new
    
    

def clear():
    return 0


def calculator():
    current_number = get_number("Enter the first number: ")

    while True:
        show_menu()
        option = input("Choose an option: ")

        if option == "1":
            new_number = get_number("Enter the other number: ")
            current_number = sum(current_number, new_number)
            print("The result is: ", current_number)
        elif option == "2":
            new_number = get_number("Enter the other number: ")
            current_number = subtract(current_number, new_number)
            print("The result is: ", current_number)
        elif option == "3":
            new_number = get_number("Enter the other number: ")
            current_number = multiplication(current_number, new_number)
            print("The result is: ", current_number)
        elif option == "4":
            new_number = get_number("Enter the other number: ")
            try:
                current_number = division(current_number, new_number)
            except ZeroDivisionError as ex:
                print("Can´t be 0: ", ex)
        elif option == "5":
            current_number = clear()
            print("The result has been cleared ", current_number) 
        elif option == "6":
            print("Finished.")
            break
        else:
            print("Invalid option")


calculator()