from functools import wraps

# Liste de livres globale
books = []

def requires_content(func):
    """Décorateur qui exécute la fonction uniquement si la liste 'books' n'est pas vide"""
    @wraps(func)
    def inner(*args, **kwargs):
        if books:
            return func(*args, **kwargs)
        else:
            return f"Erreur : aucun livre disponible pour {func.__name__}"
    
    return inner


@requires_content
def afficher_livres():
    """Affiche tous les livres disponibles"""
    return f"Livres disponibles : {', '.join(books)}"


@requires_content
def compter_livres():
    """Retourne le nombre de livres"""
    return f"Nombre de livres : {len(books)}"


@requires_content
def premier_livre():
    """Retourne le premier livre de la liste"""
    return f"Le premier livre est : {books[0]}"


# Exemples d'utilisation
if __name__ == "__main__":
    # Test 1 : sans livres (liste vide)
    print("=== Test 1 : Sans livres ===")
    print(afficher_livres())
    print(compter_livres())
    print(premier_livre())
    
    # Test 2 : avec des livres
    print("\n=== Test 2 : Avec des livres ===")
    books = ["1984", "Le Seigneur des Anneaux", "Harry Potter"]
    
    print(afficher_livres())
    print(compter_livres())
    print(premier_livre())
