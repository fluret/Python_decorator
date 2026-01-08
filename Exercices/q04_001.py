from functools import wraps


def make_type_checker(expected_type):
    """
    Fabrique de décorateurs : crée un décorateur qui valide le type 
    de l'argument unique d'une fonction.
    
    Args:
        expected_type: Le type attendu (int, str, list, dict, etc.)
    
    Returns:
        Un décorateur qui vérifie le type de l'argument avant l'exécution.
    
    Raises:
        TypeError: Si l'argument reçu n'est pas du type attendu.
    
    Example:
        check_int = make_type_checker(int)
        
        @check_int
        def double(n):
            return n * 2
        
        double(5)     # ✓ Retourne 10
        double("5")   # ✗ TypeError
    """
    def decorator(func):
        @wraps(func)
        def wrapper(arg):
            if not isinstance(arg, expected_type):
                raise TypeError(
                    f"Argument reçu: {type(arg).__name__}, "
                    f"attendu: {expected_type.__name__}"
                )
            return func(arg)
        
        return wrapper
    
    return decorator
