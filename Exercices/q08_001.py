def cache_result(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (*args, *kwargs.items())
        if key in cache:
            print("Retrieving result from cache...")
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

@cache_result
def calculate_multiply(x, y):
    print("Calculating the product of two numbers...")
    return x * y

# Call the decorated function multiple times
print(calculate_multiply(4, 5))  # Calculation is performed
print(calculate_multiply(5, 7))  # Calculation is performed
print(calculate_multiply(-3, 7))  # Calculation is performed
print(calculate_multiply(5, 7))  # Result is retrieved from cache
print(calculate_multiply(-3, 7))  # Result is retrieved from cache
print(calculate_multiply(4, 5))  # Result is retrieved from cache