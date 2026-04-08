def convert_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        with open(output_file, "w", encoding="utf-8") as new_file:
            for lines in file:
                convert = lines.upper()
                new_file.write(convert)
                print(convert)


convert_file("string.txt", "output_file_2.txt")