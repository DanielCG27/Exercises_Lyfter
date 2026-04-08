# Pida al usuario su nombre
# Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")

def get_name_age():
    name = input("Enter your name: ")
    if name.isdigit():
        raise ValueError("The name can´t be a number, try again")
    
    while True:
        try:
            age = int(input("Enter your age "))
            break
        except ValueError as ex:
            print("The value can´t be a string: ", ex)
            
    print(f"Hello {name}, your age is {age}")


while True:
    try:
        get_name_age()
        break
    except ValueError as ex:
        print(ex)