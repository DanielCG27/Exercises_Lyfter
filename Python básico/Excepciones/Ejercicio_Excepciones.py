# Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. 
# El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida,
#  o si ingresa un número invalido a la hora de hacer la operación.

def calculator():
    try:
        first_num = float(input("Place the number that you want " ))
        while (True):
            print("1. Sum\n2. Subtract\n3. Multiplication\n4. Division\n5. Clear result\n6. Exit\n")
            option = input("Choose the option: ")
            if option == "1":
                new_number = float(input("Add the other number"))
                first_num += new_number
                print("The result is: ", first_num)
            elif option == "2":
                new_number = float(input("Add the other number"))
                first_num -= new_number
                print("The result is: ", first_num)
            elif option == "3":
                new_number = float(input("Add the other number"))
                first_num *= new_number
                print("The result is: ", first_num)
            elif option == "4":
                new_number = float(input("Add the other number"))
                first_num /= new_number
                print("The result is: ", first_num)
            elif option == "5": 
                first_num = 0
                print("The result has been clear ", first_num)
            elif option == "6":
                print("Finish")
                break
            else:
                print("Invalid option")
    except ValueError as ex:
        print("Invalid number, please enter a valid number", ex)
    except ZeroDivisionError as ex:
        print("The division can´t be 0", ex)
    except Exception as ex:
        print("There is an unexpected error:", ex)


calculator()