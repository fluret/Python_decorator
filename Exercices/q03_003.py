from functools import wraps

def printer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return_value = func(*args, **kwargs)

        if return_value is not None:
            print(return_value)

    return inner
