#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

def is_prime(number):  
    if number <= 1:  
        return False
    
    for div in range(2, number):
        if number % div == 0:
            return False
        
    return True


def get_prime_numbers(numbers_list):
    prime_numbers = []

    for number in numbers_list:
        if is_prime(number):
            prime_numbers.append(number)
    
    return prime_numbers


print(get_prime_numbers([5, 2, 12, 13, 3, 17, 57]))