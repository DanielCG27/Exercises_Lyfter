# Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las 
# palabras que tengan más de n letras

def count_char(word, char):
    list = []
    
    for i in word:
        if len(i) > char:
            list.append(i)

    return list


word = input("Place your words: ")
word = word.split(",")
char = int(input("Place the number that minimal letters that you want to know: "))

print(count_char(word, char))