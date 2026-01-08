from functools import wraps

books = []

def requires_content(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if books:
            return func(*args, **kwargs)

    return inner
