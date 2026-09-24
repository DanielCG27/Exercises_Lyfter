def validate_number(func):
    def wrapper(*args, **kwargs):

        for value in args:
            if not isinstance(value, (int, float)):
                raise TypeError(f"{value} is not a number")
            
        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise TypeError(f"{value} is not a number")
            
        return func(*args, **kwargs)
    
    return wrapper

@validate_number
def multiply(a, b):
    return a * b

result = multiply(2, 8)
print(result)