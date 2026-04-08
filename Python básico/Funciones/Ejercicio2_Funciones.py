#Experimente con el concepto de scope:
#1- Intente accesar a una variable definida dentro de una función desde afuera.
#2- Intente accesar a una variable global desde una función y cambiar su valor.

def first_variable():
    variable1 = "Daniel"
    print(f"My first variable is {variable1}")


first_variable()
print(f"My first variable out the function is {variable1}") # type: ignore


# 2- Intente accesar a una variable global desde una función y cambiar su valor.

second_variable = "Hello"

def inside_function():
    print(f"My inside function is {second_variable}")


def inside_function():
    global second_variable 
    second_variable = "World"
    print(f"My inside function is {second_variable}")


inside_function()
