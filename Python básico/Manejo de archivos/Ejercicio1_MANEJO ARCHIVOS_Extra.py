# Cree un programa que lea un archivo con texto línea por línea, quite los saltos de línea (\n)
#  y escriba todo el contenido en un solo renglón en un nuevo archivo

def text_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        new_variable = []
        for line in file:
            line= line.strip()
            new_variable.append(line)

        final_variable = " ".join(new_variable)
        print(final_variable)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(final_variable)


text_file("string.txt","output_file.txt")