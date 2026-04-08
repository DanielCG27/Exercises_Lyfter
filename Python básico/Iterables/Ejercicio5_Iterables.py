numbers= []
for Q in range(10):
    num= int(input(f"Place the numbers {Q + 1}: "))
    numbers.append(num)
print(f"The numbers are: {numbers}")
max_number= max(numbers)
print(f"The highest number is {max_number}")