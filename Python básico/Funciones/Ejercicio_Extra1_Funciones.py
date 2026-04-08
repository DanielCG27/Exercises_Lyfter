#Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto

def count_character(text, char):
    count_char= 0
    for i in text:
        if i == char:
            count_char += 1

    return count_char
    

text = input("Place your word: ")
char = input("Place tha character that you want to know: ")
print(count_character(text, char))