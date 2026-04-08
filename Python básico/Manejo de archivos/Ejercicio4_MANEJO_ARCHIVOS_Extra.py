def get_text():
    first = input("Place the text that you want: ")
    return first


text = get_text()
with open("new_file.txt", "a", encoding="utf-8") as file:
    file.write(text + "\n")