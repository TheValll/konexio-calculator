# Application de Calcul de Distance avec Streamlit et Docker 🚀🌐

Cette application utilise Streamlit pour créer une interface utilisateur interactive 👨‍💻 et Docker pour faciliter le déploiement et l'exécution de l'application dans différents environnements 🐳. Elle permet de calculer la distance entre une adresse d'entreprise donnée et une liste de personnes contenue dans un fichier Excel 📊.

## Table des matières

- [Prérequis](#prérequis)
- [Installation](#installation)
- [Installation pour les non docker](#installation-pour-les-non-docker)
- [Utilisation](#utilisation)
- [Structure du fichier Excel](#structure-du-fichier-excel)

## Prérequis

- Docker 🐳 (check [Installation pour les non docker](#installation-pour-les-non-docker) si vous n'avez pas docker, python obligatoire 🐍)
- Git 📦

## Installation

1. Clonez le dépôt :
   git clone https://github.com/TheValll/konexio-calculator.git
2. Créer un fichier .env :
   ajouter un fichier .env à la racine du projet et insérer votre clé api google map. Exemple : `ACCES_API_KEY="votre cle api"` 🔑
3. Accédez au répertoire du projet :
   cd konexio
4. Construisez l'image Docker :
   docker build pull --rm -f "dockerfile" -t "cours:latest" "."
5. Exécutez le conteneur Docker :
   docker compose -f docker-compose.yml
6. Ouvrez votre navigateur et accédez à `http://localhost:8080` pour utiliser l'application 🌐.

## Installation pour les non docker

1. Clonez le dépôt :
   git clone https://github.com/TheValll/konexio-calculator.git
2. Créer un fichier .env :
   ajouter un fichier .env à la racine du projet et insérer votre clé api google map. Exemple : `ACCES_API_KEY="votre cle api"` 🔑
3. Accédez au répertoire du projet :
   cd konexio-calculator
4. Installer les dependences :
   pip install streamlit pandas openpyxl
5. Lancer l'application streamlit :
   streamlit run app/ui.py --server.port=8080 --server.address=0.0.0.0 --server.headless=True
6. Ouvrez votre navigateur et accédez à `http://localhost:8080` pour utiliser l'application 🌐.

## Utilisation

1. Accédez à l'application via votre navigateur.
2. Téléchargez votre fichier Excel contenant la liste des personnes.
3. Entrez l'adresse de l'entreprise pour laquelle vous souhaitez calculer la distance.
4. Cliquez sur le bouton "Calculer la distance" pour obtenir les résultats 📏.

## Structure du fichier Excel

Le fichier Excel doit contenir les colonnes suivantes :

- Nom
- Prénom
- Adresse
- Code postal
- Ville

Exemple de structure :

| Nom    | Prénom | Adresse               | Code postal | Ville |
| ------ | ------ | --------------------- | ----------- | ----- |
| Dupont | Jean   | 123 Rue de la Paix    | 75000       | Paris |
| Martin | Marie  | 456 Rue de la Liberté | 69000       | Lyon  |
