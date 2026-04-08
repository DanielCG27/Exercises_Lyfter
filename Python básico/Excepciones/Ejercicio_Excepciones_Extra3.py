def sum_values(string_list):
    total_sum = 0
    for element in string_list:
        try:
            number = float(element)
            total_sum += number
            print(f"{element} Summed correctly")
        except ValueError:
            print(f"Invalid element: {element}")

    print(f"Total sum: ", total_sum)


string_list = [10, "Hola", 25.5, "Sol", 3.7]
sum_values(string_list)