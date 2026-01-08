from q03_003 import printer


@printer
def dire_bonjour(nom: str):
    return f"Bonjour, {nom}!"


@printer
def addition(a: int, b: int):
    if a > 0:
        return f"{a} + {b} = {a + b}"


@printer
def ne_retourne_rien():
    # Cette fonction ne retourne rien, le décorateur ne devrait rien afficher
    return None


if __name__ == "__main__":
    print("=== Test du décorateur printer (q03-003.py) ===")
    dire_bonjour("Alice")
    addition(3, 4)
    ne_retourne_rien()
    addition(-1, 5)  # Ne devrait rien afficher car a <= 0
