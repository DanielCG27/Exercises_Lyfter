time= int(input("Place the number in seconds"))
if time < 600:
    answer= 600 - time
elif time > 600:
    answer= "Greater"
else:
    answer= "Equal"
print(f"The answer is {answer}")