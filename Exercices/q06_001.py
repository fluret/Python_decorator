from functools import wraps
from q06_002 import make_html

@make_html('p')
@make_html('strong', class_='bold', id='main-text')
def get_text(text):
    return text

print(get_text('I code with PyBites'))