# Module : templates

## 1. Raison d’être

Ce répertoire contient les fichiers de présentation (vues) de l’application web.
Il définit la structure HTML affichée à l’utilisateur et assure l’interface
entre le backend Flask et l’interface graphique.

Ce module est responsable de l’affichage dynamique des données transmises
par les routes Flask.

---

## 2. Fichiers principaux et responsabilités

- `index.html`  
  Définit la structure de l’interface utilisateur de la calculatrice.
  Ce fichier est responsable de :
  - L’affichage du titre de l’application
  - La création du formulaire envoyé en méthode POST
  - L’affichage du champ de saisie et du résultat
  - La disposition des boutons numériques et opérateurs
  - L’intégration du style via le fichier `style.css`
  - L’affichage dynamique du résultat
  - La gestion des interactions côté client à l’aide de fonctions JavaScript

---

## 3. Dépendances et hypothèses

- Dépend du framework Flask pour le rendu des templates (`render_template`)
- Utilise le moteur de templating Jinja pour injecter dynamiquement les données
- Dépend du fichier `style.css` situé dans le dossier `static`
- Suppose que la route principale transmet une variable `result`
