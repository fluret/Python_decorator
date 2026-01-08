@validate_arguments(lambda x: x > 0)
def calculate_cube(x):
    return x ** 3

print(calculate_cube(5))  # Output: 125
print(calculate_cube(-2))  # Raises ValueError: Invalid arguments passed to the function