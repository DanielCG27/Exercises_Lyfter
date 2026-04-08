numbers= [25, 3, 8, 94, 50, 4]
minor= float("inf")
for num in numbers:
    if num < minor:
        minor = num
print("The smallest value is:", minor)