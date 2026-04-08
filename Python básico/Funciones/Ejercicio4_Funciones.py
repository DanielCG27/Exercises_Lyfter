#Cree una función que le de la vuelta a un string y lo retorne.

def reversed_word():
    word = "Programming"
    reversed_word = ""


    for i in word:
        reversed_word = i + reversed_word
        
    return reversed_word

print(reversed_word())