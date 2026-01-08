from q04_001 import make_type_checker


# Création des décorateurs spécialisés
check_int = make_type_checker(int)
check_str = make_type_checker(str)
check_list = make_type_checker(list)
check_dict = make_type_checker(dict)
check_float = make_type_checker(float)


# Test 1 : Validation d'entier
@check_int
def double(n):
    """Retourne le double d'un nombre."""
    return n * 2


# Test 2 : Validation de chaîne
@check_str
def uppercase(text):
    """Convertit en majuscules."""
    return text.upper()


# Test 3 : Validation de liste
@check_list
def count_items(items):
    """Compte les éléments."""
    return len(items)


# Test 4 : Validation de dictionnaire
@check_dict
def get_keys(d):
    """Retourne les clés du dictionnaire."""
    return list(d.keys())


# Test 5 : Validation de float
@check_float
def sqrt_approx(x):
    """Retourne la racine carrée approximée."""
    return x ** 0.5


# Test 6 : Préservation des métadonnées
@check_int
def square(x):
    """Élève au carré."""
    return x ** 2


if __name__ == "__main__":
    print("=== Test 1 : Validation d'entier ===")
    try:
        result = double(5)
        print(f"✓ double(5) = {result}")
    except TypeError as e:
        print(f"✗ Erreur: {e}")
    
    try:
        result = double("5")
        print(f"✓ double('5') = {result}")
    except TypeError as e:
        print(f"✗ Erreur attendu: {e}")
    
    print("\n=== Test 2 : Validation de chaîne ===")
    try:
        result = uppercase("hello")
        print(f"✓ uppercase('hello') = {result}")
    except TypeError as e:
        print(f"✗ Erreur: {e}")
    
    try:
        result = uppercase(123)
        print(f"✓ uppercase(123) = {result}")
    except TypeError as e:
        print(f"✗ Erreur attendu: {e}")
    
    print("\n=== Test 3 : Validation de liste ===")
    try:
        result = count_items([1, 2, 3])
        print(f"✓ count_items([1, 2, 3]) = {result}")
    except TypeError as e:
        print(f"✗ Erreur: {e}")
    
    try:
        result = count_items("abc")
        print(f"✓ count_items('abc') = {result}")
    except TypeError as e:
        print(f"✗ Erreur attendu: {e}")
    
    print("\n=== Test 4 : Validation de dictionnaire ===")
    try:
        result = get_keys({"a": 1, "b": 2})
        print(f"✓ get_keys({{'a': 1, 'b': 2}}) = {result}")
    except TypeError as e:
        print(f"✗ Erreur: {e}")
    
    try:
        result = get_keys([1, 2, 3])
        print(f"✓ get_keys([1, 2, 3]) = {result}")
    except TypeError as e:
        print(f"✗ Erreur attendu: {e}")
    
    print("\n=== Test 5 : Validation de float ===")
    try:
        result = sqrt_approx(9.0)
        print(f"✓ sqrt_approx(9.0) = {result}")
    except TypeError as e:
        print(f"✗ Erreur: {e}")
    
    try:
        result = sqrt_approx([9])
        print(f"✓ sqrt_approx([9]) = {result}")
    except TypeError as e:
        print(f"✗ Erreur attendu: {e}")
    
    print("\n=== Test 6 : Préservation de __name__ et __doc__ ===")
    print(f"Nom: {square.__name__}")
    print(f"Doc: {square.__doc__}")
    
    print("\n=== Test 7 : Utilisation correcte ===")
    try:
        result = square(4)
        print(f"✓ square(4) = {result}")
    except TypeError as e:
        print(f"✗ Erreur: {e}")
    
    print("\n=== Test 8 : Réutilisabilité de la fabrique ===")
    check_bool = make_type_checker(bool)
    
    @check_bool
    def negate(value):
        return not value
    
    try:
        result = negate(True)
        print(f"✓ negate(True) = {result}")
    except TypeError as e:
        print(f"✗ Erreur: {e}")
    
    try:
        result = negate(1)  # 1 n'est pas un bool
        print(f"✓ negate(1) = {result}")
    except TypeError as e:
        print(f"✗ Erreur attendu: {e}")
