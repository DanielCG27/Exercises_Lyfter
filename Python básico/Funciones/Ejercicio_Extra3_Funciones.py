# Cree una función que reciba un string y retorne cuántas vocales contiene

def word(vowels):
    count_vowels = 0
    list_vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for i in vowels:
        if i in list_vowels:
            count_vowels += 1
    return count_vowels


vowels = input("Place your word: ")
print(word(vowels))
