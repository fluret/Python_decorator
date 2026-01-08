from functools import wraps

def strip_range(start, end):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            text = func(*args, **kwargs)
            return text[:start] + "." * (end - start) + text[end:]
        return wrapper
    return decorator

# Test cases
def test_strip_range():
    @strip_range(3, 5)
    def gen_output(text):
        return text
    
    assert gen_output("Hello world") == "Hel.. world"
    assert gen_output("Python") == "Pyt..n"
    assert gen_output("123456789") == "123..6789"
    assert gen_output("abcdefg") == "abc..fg"
    print("All tests passed!")

test_strip_range()    