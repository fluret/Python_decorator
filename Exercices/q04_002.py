from q04_001 import make_type_checker

check_int = make_type_checker(int)

# Test 1 : Validation d'entier
@check_int
def double(n):
    """Retourne le double d'un nombre."""
    return n * 2

# Test 2 : Validation de chaîne

# Test 3 : Validation de liste

# Test 4 : Validation de dictionnaire

# Test 5 : Validation de float

# Test 6 : Préservation des métadonnées

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
