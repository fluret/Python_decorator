from functools import wraps
import inspect


def type_check(_func=None, **type_specs):
    """
    Décorateur qui valide les types des arguments et du retour d'une fonction.
    
    Usage avec paramètres:
        @type_check(a=int, b=str, return_type=list)
        def ma_fonction(a, b):
            return [a, b]
    
    Usage sans paramètres (utilise les annotations):
        @type_check
        def ma_fonction(a: int, b: str) -> list:
            return [a, b]
    
    Args:
        **type_specs: Spécification des types. Les clés sont les noms des paramètres,
                      la clé spéciale 'return_type' définit le type de retour attendu.
    """
    def decorator(func):
        # Récupérer les annotations de la fonction (bonus)
        annotations = getattr(func, '__annotations__', {})
        
        # Fusionner les spécifications: annotations en tant que défaut, type_specs en priorité
        specs = annotations.copy()
        specs.update(type_specs)
        
        # Séparer le type de retour des paramètres
        return_type = specs.pop('return_type', None) or specs.pop('return', None)
        param_types = specs
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Obtenir la signature de la fonction
            sig = inspect.signature(func)
            
            # Lier les arguments à la signature
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # Valider chaque argument
            for param_name, param_value in bound_args.arguments.items():
                if param_name in param_types:
                    expected_type = param_types[param_name]
                    if not isinstance(param_value, expected_type):
                        raise TypeError(
                            f"Argument '{param_name}' attendu {expected_type.__name__}, "
                            f"reçu {type(param_value).__name__}"
                        )
            
            # Exécuter la fonction
            result = func(*args, **kwargs)
            
            # Valider le type de retour si spécifié
            if return_type is not None:
                if not isinstance(result, return_type):
                    raise TypeError(
                        f"Retour attendu {return_type.__name__}, "
                        f"reçu {type(result).__name__}"
                    )
            
            return result
        
        return wrapper
    
    return decorator
    
    # Si appelé sans parenthèses: @type_check
    if _func is not None:
        return decorator(_func)
    # Si appelé avec parenthèses: @type_check(...)
    else:
        return decorator
