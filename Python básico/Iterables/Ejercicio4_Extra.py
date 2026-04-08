def calculate_average(list):
    return sum(list) / len(list)
def higher_values_average(list):
    average= calculate_average(list)
    return [num for num in list if num > average]
num= [80, 23, 98, 41, 12]
average= calculate_average(num)
higher_average= higher_values_average(num)
print("The list average is:", average)
print("Higher than average values:", higher_average)