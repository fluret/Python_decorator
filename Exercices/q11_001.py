def add_logging(func):
    def wrapper(*args, **kwargs):
        # Log the function name and arguments
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Log the return value
        print(f"{func.__name__} returned: {result}")
        
        # Return the result
        return result
    return wrapper

# Example usage
@add_logging
def add_numbers(x, y):
    return x + y

# Call the decorated function
result = add_numbers(200, 300)
print("Result:", result)
