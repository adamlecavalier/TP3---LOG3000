from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str) -> float:
    '''
    Analyse une chaîne de de caractères pour effectuer une opération mathématique
    simple (ex: "3 + 4") et retourne le résultat numérique.

    Paramètres:
        expr (str): Expression mathématique contenant deux opérandes
                    numériques et un seul opérateur supporté.

    Retour:
        float: Résultat de l'opération mathématique.

    Exceptions:
        ValueError: Si l'expression est vide, mal formée, contient plus d'un
                    opérateur, ou si les opérandes ne sont pas des nombres.
    '''
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # Cette vérification assure qu'il y a exactement deux opérandes dans l'expression
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    '''
    Gère la route principale de l'application web de calculatrice.

    Méthodes HTTP:
    GET : Affiche la page initiale avec un affichage vide.
    POST : Récupère l'expression envoyée par le formulaire,
            appelle la fonction de calcul et affiche le résultat.

    Entrées:
        Reçoit une donnée de formulaire nommée 'display' contenant
        l'expression mathématique saisie par l'utilisateur.

    Retour:
        Page HTML 'index.html' rendue avec le résultat du calcul
        ou un message d'erreur si l'expression est invalide.
    '''
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)