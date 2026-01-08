from functools import wraps

def make_html(tag, **attrs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Supprimer le _ final des clés (pour éviter les mots-clés Python)
            clean_attrs = {key.rstrip('_'): value for key, value in attrs.items()}
            attributes = " ".join(f'{key}="{value}"' for key, value in clean_attrs.items())
            attr_str = f" {attributes}" if attributes else ""
            return f"<{tag}{attr_str}>{func(*args, **kwargs)}</{tag}>"
        return wrapper
    return decorator

if __name__ == "__main__":
    def test_make_html():
        @make_html('p')
        @make_html('strong', class_='bold', id='main-text')
        def get_text(text='I code with PyBites'):
            return text
        
        assert get_text() == '<p><strong class="bold" id="main-text">I code with PyBites</strong></p>'
        print("HTML wrapping test passed!")
        
    test_make_html()