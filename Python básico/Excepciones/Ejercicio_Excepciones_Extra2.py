def convert_integer(string_list):
    for i in string_list:
        try:
            number = int(i)
            print(f"{i} converted to {number}")
        except ValueError:
            print(f"Could not convert the element: {i}")


string_list = ["4.8", "Mountain", "10", "67"]
convert_integer(string_list)