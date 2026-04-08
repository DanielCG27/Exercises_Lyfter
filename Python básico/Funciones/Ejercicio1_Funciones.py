#Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
def dog_name():
    name = str(input("Place the dog name"))


    print(f"The dog name is {name}")
    
    #Second function
    cat_name()


def cat_name():
    name_cat = str(input("Place the cat name"))


    print(f"The cat name is {name_cat}")


dog_name()