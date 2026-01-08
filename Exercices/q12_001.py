import math

def handle_exceptions(default_response=""):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                # Call the original function
                return func(*args, **kwargs)
            except Exception as e:
                # Handle the exception and provide the default response
                print(f"Exception occurred: {e}")
                if default_response != "":
                    return default_response
                else:
                    return "Opération impossible"
        return wrapper
    return decorator

@handle_exceptions(default_response="An error occurred!")
def divide_numbers(x, y):
    return x / y

@handle_exceptions()
def racine(x):
    return math.sqrt(x)


result = divide_numbers(7, 0)  # This will raise a ZeroDivisionError
print("Result:", result)
print('************')
result = divide_numbers(8, 2)  # This will not raise an error
print("Result:", result)
print('************')
result = racine(-4)  # This will raise a ValueError
print("Result:", result)