# Flask Calculator

## Équipe 31

## Objectif
Ce projet vise à développer et maintenir une **application web de calculatrice simple** basée sur le framework **Flask (Python)**.

L’objectif est de :
- Comprendre une base de code existante
- Corriger les bogues présents
- Ajouter des tests automatisés
- Mettre en place de bonnes pratiques de gestion de versions
- Documenter clairement le projet pour faciliter son utilisation et sa maintenance

---

## Prérequis d'installation

Avant de configurer le projet, assurez-vous d'avoir

* **Un compte GitHub**
* **Git installé localement**
* **Python et pip installés**

---

## Instructions d'installation

Suivez les étapes ci-dessous pour exécuter le projet localement.

### 1. Cloner le dépot

Dans un terminal, exécutez :

    git clone https://github.com/adamlecavalier/TP3---LOG3000.git

### 2. Ouvrir le projet

Ouvrez le répertoire `TP3---LOG3000` dans **VS Code** ou l'éditeur de votre choix.

### 3. Installer les dépendances
Pour installer Flask, il suffit d'exécuter cette commande dans un terminal du répertoire: 

    pip install flask

### 4. Démarrer le serveur Flask
Pour démarrer le serveur local, assurez vous d'être dans le répertoire principal du projet, soit TP3---LOG3000. Ensuite, exécutez la commande suivante: 

    python app.py

### 5. Accéder à l'application
Une fois le message ``Running on http://127.0.0.1:5000`` affiché dans le terminal, ouvrez votre navigateur et accédez à l'URL suivante : http://127.0.0.1:5000

## Utilisation des fonctionnalités

Une fois que le serveur est lancé localement et que vous êtes sur l'adresse locale (http://127.0.0.1:5000), vous pouvez commencer à utiliser l'application :

* **Effectuer un calcul** : Entrez deux nombres entiers positifs dans les cases de saisie.
* **Choisir une opération** : Cliquez sur l'opération désirée (Addition, Soustraction, etc.).
* **Visualiser le résultat** : Le résultat s'affiche sous les champs de saisie après avoir cliqué sur le bouton de validation.

## Exécution des tests
Pour exécuter la suite de tests, il faut faire cette commande: 

    python -m unittest discover tests

Le résultat des tests se retrouvent dans le terminal où la commande a été exécutée.

## Flux de contribution

Pour assurer une collaboration efficace au sein de l'équipe, nous suivons ce flux de travail :

### 1. Gestion des Issues
* Avant de commencer un travail, vérifiez les **Issues** sur GitHub pour voir les tâches assignées ou les bogues répertoriés.
* Créez une nouvelle Issue pour tout bogue découvert ou nouvelle fonctionnalité proposée.

### 2. Création de branches
Ne travaillez jamais directement sur la branche `main`. Créez une branche descriptive pour chaque tâche :

    git checkout -b nom-de-votre-branche

### 3. Pull Requests (PR)
* Une fois vos modifications terminées et testées localement, poussez votre branche sur GitHub.
* Ouvrez une **Pull Request** vers la branche `main`.
* La PR doit être révisée par au moins un autre membre de l'équipe avant d'être fusionnée.

### 4. Fusion (Merge)
* Après approbation et succès des tests, la branche est fusionnée et supprimée pour garder le dépôt propre.