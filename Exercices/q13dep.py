@cache_with_expiry(expiry_time=5)  # Cache expiry time set to 5 seconds
def calculate_multiply(x, y):
    print("Calculating product of two numbers...")
    return x * y

print(calculate_multiply(23, 5))  # Calculation is performed
print(calculate_multiply(23, 5))  # Result is retrieved from cache
print("wait for cache to expire...")
time.sleep(5)
print(calculate_multiply(23, 5))  # Calculation is performed (cache expired)