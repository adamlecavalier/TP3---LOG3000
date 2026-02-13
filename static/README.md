# Module : static

## 1. Raison d’être

Ce répertoire contient les ressources statiques de l’application web.
Il regroupe les fichiers utilisés par l’interface utilisateur, mais qui ne
sont pas générés dynamiquement par Flask.

## 2. Fichiers principaux et responsabilités

- `style.css`  
  Définit l’apparence visuelle de la calculatrice et assure la séparation
  entre la logique backend et la présentation frontend.  
  Il est responsable de :
  - La mise en page centrée de l’interface
  - Le style et le comportement visuel des boutons
  - L’apparence du champ d’affichage
  - La gestion des états interactifs (hover, active)
  - L’ergonomie générale de l’application


## 3. Dépendances et hypothèses

- Utilisé par `index.html` via `url_for('static', filename='style.css')`
- Suppose la présence des classes HTML suivantes :
  - `.calculator`
  - `.buttons`
  - `.btn`
  - `.operator`
