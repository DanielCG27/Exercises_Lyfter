import random
secret_number= random.randint(1, 10)
while True:
    attempt= int(input("Guess the number (1 to 10):"))
    if attempt < secret_number:
        print("Too low, try again")
    elif attempt > secret_number:
        print("Too hight, try again")
    else:
        print("Correct, you guessed the number")
        break