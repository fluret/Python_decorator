from functools import wraps

def convert_to_data_type(data_type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return data_type(result)
        return wrapper
    return decorator

liste = [[10, 20], [30, 40], ["50", "60"], ["70", "80"]]

for a, b in liste:
    @convert_to_data_type(int)
    def add(x, y):
        return x + y
    
    def add_2(x, y):
        return x + y
    result = add(a, b)
    result_2 = add_2(a, b)
    print("Result:", result, type(result))
    print("Result 2:", result_2, type(result_2))