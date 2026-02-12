def add(a: float,b: float) -> float:
    '''
    Additionne deux nombres.
    
    Paramètres:
        a (float): Premier opérande.
        b (float): Deuxième opérande.
    
    Retour:
        float: Somme de a et b.
    '''
    return a + b

def subtract(a: float,b: float) -> float:
    '''
    Soustraction de deux nombres.

    Paramètres:
        a (float): Nombre à soustraire.
        b (float): Nombre duquel on soustrait.
    
    Retour:
        float: Résultat de b - a.
    '''
    return b - a

def multiply(a: float,b: float) -> float:
    '''
    Multiplication de deux nombres.

    Paramètres:
        a (float): Premier opérande.
        b (float): Deuxième opérande.
    
    Retour:
        float: Produit de a et b.
    '''
    return a ** b

def divide(a: float,b: float) -> float:
    '''
    Division de deux nombres.

    Paramètres:
        a (float): Dividende.
        b (float): Diviseur.

    Retour:
        float: Résultat de a // b.
    '''
    return a // b
