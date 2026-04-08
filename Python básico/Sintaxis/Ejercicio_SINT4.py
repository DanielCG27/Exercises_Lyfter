first_int= int(input("Coloque su primer número"))
second_int= int(input("Coloque su segundo número"))
third_int= int(input("Coloque su tercer número"))
if first_int >= second_int and first_int >= third_int:
    largest= first_int
elif second_int >= first_int and second_int >= third_int:
    largest= second_int
else:
    largest= third_int
print("The largest number is:", largest)