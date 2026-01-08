@cache_result
def calculate_multiply(x, y):
    print("Calculating the product of two numbers...")
    return x * y

print(calculate_multiply(4, 5))  # Calculation is performed
print(calculate_multiply(4, 5))  # Result is retrieved from cache
print(calculate_multiply(5, 7))  # Calculation is performed
print(calculate_multiply(5, 7))  # Result is retrieved from cache
print(calculate_multiply(-3, 7))  # Calculation is performed
print(calculate_multiply(-3, 7))  # Result is retrieved from cache