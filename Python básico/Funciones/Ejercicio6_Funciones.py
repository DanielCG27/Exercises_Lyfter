#Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente
# Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.

def separate_words(my_list):
    my_list = "Dog-Otter-Cat-Dolphin"
    my_other_list = my_list.split("-")
    my_other_list.sort()
    result = "-".join(my_other_list)
    return result


print(separate_words(""))
