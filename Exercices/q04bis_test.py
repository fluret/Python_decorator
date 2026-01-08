from q04bis_002 import type_check


# Test 1 : Spécification explicite avec arguments positionnels
@type_check(a=int, b=str, return_type=str)
def concat(a, b):
    """Concatène un entier et une chaîne."""
    return f"{a}:{b}"


# Test 2 : Avec annotations Python (bonus)
@type_check
def somme(a: int, b: int) -> int:
    """Additionne deux entiers."""
    return a + b


# Test 3 : Arguments nommés
@type_check(x=int, y=int, return_type=int)
def multiplier(x, y):
    """Multiplie deux entiers."""
    return x * y


# Test 4 : Paramètres avec valeurs par défaut
@type_check(nom=str, age=int)
def afficher_personne(nom, age=18):
    """Affiche les infos d'une personne."""
    return f"{nom} a {age} ans"


# Test 5 : Type de retour incorrect (volontairement)
@type_check(vals=list, return_type=int)
def count(vals):
    """Retourne le nombre d'éléments."""
    return len(vals)


# Test 6 : Validation du type liste
@type_check(items=list, return_type=int)
def sum_list(items):
    """Somme les éléments d'une liste."""
    return sum(items)


if __name__ == "__main__":
    print("=== Test 1 : Spécification explicite ===")
    try:
        print(concat(3, "x"))  # ✓ Passe
        print("✓ concat(3, 'x') OK")
    except TypeError as e:
        print(f"✗ Erreur: {e}")
    
    try:
        print(concat("3", "x"))  # ✗ TypeError
        print("✓ concat('3', 'x') OK")
    except TypeError as e:
        print(f"✗ Erreur attendu: {e}")
    
    print("\n=== Test 2 : Avec annotations Python ===")
    try:
        print(somme(1, 2))  # ✓ Passe
        print("✓ somme(1, 2) OK")
    except TypeError as e:
        print(f"✗ Erreur: {e}")
    
    try:
        print(somme(1, "2"))  # ✗ TypeError
        print("✓ somme(1, '2') OK")
    except TypeError as e:
        print(f"✗ Erreur attendu: {e}")
    
    print("\n=== Test 3 : Arguments nommés ===")
    try:
        print(multiplier(x=2, y=3))  # ✓ Passe
        print("✓ multiplier(x=2, y=3) OK")
    except TypeError as e:
        print(f"✗ Erreur: {e}")
    
    try:
        print(multiplier(2, "3"))  # ✗ TypeError
        print("✓ multiplier(2, '3') OK")
    except TypeError as e:
        print(f"✗ Erreur attendu: {e}")
    
    print("\n=== Test 4 : Valeurs par défaut ===")
    try:
        print(afficher_personne("Alice"))  # ✓ Passe (age=18 par défaut)
        print("✓ afficher_personne('Alice') OK")
    except TypeError as e:
        print(f"✗ Erreur: {e}")
    
    try:
        print(afficher_personne("Bob", 25))  # ✓ Passe
        print("✓ afficher_personne('Bob', 25) OK")
    except TypeError as e:
        print(f"✗ Erreur: {e}")
    
    print("\n=== Test 5 : Validation du type de retour ===")
    try:
        print(count([1, 2, 3]))  # ✓ Passe (retourne int)
        print("✓ count([1, 2, 3]) OK")
    except TypeError as e:
        print(f"✗ Erreur: {e}")
    
    try:
        print(count("abc"))  # ✗ TypeError (argument incorrect)
        print("✓ count('abc') OK")
    except TypeError as e:
        print(f"✗ Erreur attendu: {e}")
    
    print("\n=== Test 6 : Préservation __name__ et __doc__ ===")
    print(f"Nom: {concat.__name__}")
    print(f"Doc: {concat.__doc__}")
    print(f"Nom: {somme.__name__}")
    print(f"Doc: {somme.__doc__}")
    
    print("\n=== Test 7 : Sum list ===")
    try:
        print(sum_list([1, 2, 3]))  # ✓ Passe
        print("✓ sum_list([1, 2, 3]) OK")
    except TypeError as e:
        print(f"✗ Erreur: {e}")
