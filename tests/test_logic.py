import unittest
from operators import add, subtract, multiply, divide
from app import calculate

class TestCalculator(unittest.TestCase):
    """
    Classe de test unitaire pour valider la logique de calcul de l'application
    """
    def test_add(self):
        """Vérifie que l'addition de deux nombres retourne la somme correcte."""
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        """Vérifie que la soustraction retourne la différence exacte."""
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        """Vérifie que la multiplication retourne le produit exact."""
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        """Vérifie que la division retourne un quotient réel (float)."""
        self.assertEqual(divide(10, 4), 2.5)
        
    def test_divide_by_zero(self):
        """Vérifie que la division par zéro lève l'exception ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_calculate_invalid_format(self):
        """Vérifie qu'une expression avec plus d'un opérateur lève une ValueError."""
        with self.assertRaises(ValueError):
            calculate("10 + 5 + 2")

    def test_calculate_non_numeric(self):
        """Vérifie que l'utilisation de caractères alphabétiques lève une ValueError."""
        with self.assertRaises(ValueError):
            calculate("10 + abc")

    def test_calculate_empty(self):
        """Vérifie qu'une chaîne vide ou invalide lève une erreur appropriée."""
        with self.assertRaises(ValueError):
            calculate("")

if __name__ == '__main__':
    unittest.main()