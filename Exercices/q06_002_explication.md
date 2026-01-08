# Explication détaillée du décorateur `make_html`

## Vue d'ensemble
Ce code implémente une **fabrique de décorateurs** qui enveloppe le résultat d'une fonction dans des balises HTML. C'est un exemple de **décorateur paramétré** en Python.

---

## Structure générale : 3 niveaux d'imbrication

```
make_html(tag, **attrs)           # Niveau 1 : Fabrique
    └─ decorator(func)             # Niveau 2 : Décorateur
        └─ wrapper(*args, **kwargs) # Niveau 3 : Wrapper (exécuté à chaque appel)
```

### Pourquoi 3 niveaux ?
- Le décorateur est **paramétré** : il reçoit `tag` (la balise HTML) et `**attrs` (les attributs HTML).
- Avec des paramètres, il faut une fabrique (niveau 1) pour capturer ces valeurs avant de retourner le décorateur réel.

---

## Niveau 1 : La fabrique `make_html(tag, **attrs)`

```python
def make_html(tag, **attrs):
```

**Rôle** : Accepter les paramètres du décorateur.

**Paramètres** :
- `tag` : une chaîne représentant la balise HTML (ex: `'p'`, `'strong'`, `'div'`)
- `**attrs` : arguments nommés arbitraires représentant les attributs HTML (ex: `class_='bold'`, `id='main-text'`)

**Exemple d'appel** :
```python
make_html('p')  # tag='p', attrs={}
make_html('strong', class_='bold', id='main-text')  # tag='strong', attrs={'class_': 'bold', 'id': 'main-text'}
```

Ces valeurs sont **capturées** dans la fermeture (closure) des fonctions internes.

---

## Niveau 2 : Le décorateur `decorator(func)`

```python
def decorator(func):
```

**Rôle** : Être le véritable décorateur que Python applique à la fonction.

**Paramètre** :
- `func` : la fonction décorée (passée automatiquement par Python lors du décorateur)

**Exemple** :
```python
@make_html('strong', class_='bold', id='main-text')
def get_text(text='I code with PyBites'):
    return text

# Python appelle : decorator(get_text)
# où decorator est ce qu'a retourné make_html('strong', class_='bold', id='main-text')
```

À l'intérieur, on défini le wrapper et on le retourne avec `@wraps(func)`.

### `@wraps(func)` : Préserver les métadonnées

```python
@wraps(func)
def wrapper(*args, **kwargs):
```

`@wraps(func)` copie les métadonnées de `func` au `wrapper` :
- `wrapper.__name__` = `func.__name__`
- `wrapper.__doc__` = `func.__doc__`
- Autres attributs importants

**Sans `@wraps`** : on perdrait le nom et la doc de la fonction décorée. Essentiel pour la maintenabilité.

---

## Niveau 3 : Le wrapper `wrapper(*args, **kwargs)`

```python
def wrapper(*args, **kwargs):
```

**Rôle** : C'est la fonction qui s'exécute **à chaque appel** de la fonction décorée.

### Étape 1 : Nettoyer les attributs

```python
clean_attrs = {key.rstrip('_'): value for key, value in attrs.items()}
```

**Pourquoi ?** En Python, `class`, `for`, `if` sont des mots-clés réservés. On ne peut pas passer `class='bold'` directement.

**Solution** : On passe `class_='bold'` (avec un tiret bas). Cette ligne supprime le tiret bas final.

**Exemple** :
```python
attrs = {'class_': 'bold', 'id': 'main-text'}
clean_attrs = {'class': 'bold', 'id': 'main-text'}
```

### Étape 2 : Construire la chaîne d'attributs HTML

```python
attributes = " ".join(f'{key}="{value}"' for key, value in clean_attrs.items())
```

Crée une chaîne des attributs au format HTML.

**Exemple** :
```python
clean_attrs = {'class': 'bold', 'id': 'main-text'}
attributes = 'class="bold" id="main-text"'
```

**Comment ça marche** :
- Boucle sur chaque paire clé-valeur
- Formate comme `key="value"`
- Jointure avec des espaces

### Étape 3 : Ajouter un espace si des attributs existent

```python
attr_str = f" {attributes}" if attributes else ""
```

Si des attributs existent, on ajoute un espace devant pour séparer la balise des attributs.

**Exemples** :
```python
# Avec attributs
attr_str = " class=\"bold\" id=\"main-text\""

# Sans attributs
attr_str = ""
```

### Étape 4 : Envelopper le résultat dans la balise HTML

```python
return f"<{tag}{attr_str}>{func(*args, **kwargs)}</{tag}>"
```

Exécute la fonction décorée, enveloppe son résultat dans les balises HTML.

**Flux complet** :
1. `func(*args, **kwargs)` exécute la fonction décorée et récupère son résultat
2. Construit la balise ouvrante : `<{tag}{attr_str}>` ex: `<strong class="bold" id="main-text">`
3. Insère le résultat de la fonction
4. Ajoute la balise fermante : `</{tag}>` ex: `</strong>`

**Exemple concret** :
```python
func() retourne : "I code with PyBites"
tag = "strong"
attr_str = " class=\"bold\" id=\"main-text\""

Résultat final : '<strong class="bold" id="main-text">I code with PyBites</strong>'
```

---

## Exemple d'exécution complète

```python
@make_html('p')
@make_html('strong', class_='bold', id='main-text')
def get_text(text='I code with PyBites'):
    return text
```

**Déroulement** :

1. **Appel** : `get_text()`

2. **Premier wrapper** (le plus interne, `strong`) :
   - Exécute `get_text()` → `"I code with PyBites"`
   - Enveloppe avec `<strong class="bold" id="main-text">...</strong>`
   - Retourne : `'<strong class="bold" id="main-text">I code with PyBites</strong>'`

3. **Deuxième wrapper** (`p`) :
   - Exécute le résultat du wrapper précédent
   - Enveloppe avec `<p>...</p>`
   - Retourne : `'<p><strong class="bold" id="main-text">I code with PyBites</strong></p>'`

4. **Résultat final** : `'<p><strong class="bold" id="main-text">I code with PyBites</strong></p>'`

---

## Avantages de cette approche

✓ **Réutilisabilité** : On peut l'appliquer à plusieurs fonctions
✓ **Flexibilité** : Changer la balise ou les attributs sans modifier la fonction
✓ **Composition** : Plusieurs décorateurs imbriqués pour combiner des balises
✓ **Séparation** : La logique HTML est séparée de la logique métier

---

## Résumé

Ce décorateur paramétré utilise 3 niveaux :
- **Fabrique** : capture les paramètres (`tag`, `attrs`)
- **Décorateur** : s'applique à la fonction
- **Wrapper** : enveloppe le résultat dans du HTML à chaque exécution
