# Documentation des Tests

Ce répertoire contient la suite de tests unitaires pour l'application Flask Calculator.

## Objectif des tests
L'objectif est de garantir que le moteur de calcul (`calculate`) et les fonctions mathématiques de base (`operators.py`) fonctionnent correctement et gèrent les erreurs de saisie sans faire planter le serveur.

## Couverture des tests
Les fichiers de test couvrent les aspects suivants :
* **Fonctions de base** : Addition, soustraction, multiplication, division.
* **Gestion des erreurs fatales** : Division par zéro.
* **Parsing d'expression** :
  * Validation du format (un seul opérateur autorisé).
  * Rejet des caractères non numériques.

## Comment exécuter les tests

Pour lancer tous les tests à partir de la racine du projet, utilisez la commande suivante :

    `python -m unittest discover tests`
