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