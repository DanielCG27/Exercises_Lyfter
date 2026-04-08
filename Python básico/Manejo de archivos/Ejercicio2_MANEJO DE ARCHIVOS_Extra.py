# Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.

def count_words(file_path):
    with open(file_path,"r", encoding="utf-8") as file:
        quantity_text = file.read()
        new_quantity_text = quantity_text.split()
        new_quantity_text_2 = len(new_quantity_text)
    print(f"This file has {new_quantity_text_2} words")


count_words("string.txt")