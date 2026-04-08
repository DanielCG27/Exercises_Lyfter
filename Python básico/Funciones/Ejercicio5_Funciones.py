# Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.

def count_types_letters():
    uppercase_count = 0
    lowercase_count = 0
    word = "CostA Rica"
    for types in word:
        if types.isupper():
            uppercase_count += 1
        elif types.islower():
            lowercase_count += 1


    print(f"The uppercase quantity are:", uppercase_count)
    print(f"The lowercase quantity are", lowercase_count)


count_types_letters()