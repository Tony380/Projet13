# Projet 13 [![Build Status](https://travis-ci.org/Tony380/Projet13.svg?branch=main)](https://travis-ci.org/Tony380/Projet13)


Projet final du parcours "développeur d'application Python" d'Openclassrooms

## Présentation
France2020 est une application qui permet d'apprendre la géographie de la France métropolitaine
avec des cartes interactives et des articles de Wikipédia.

Pour cela, l'application utilise les API de Wikipédia et de Google Maps.

La première carte présente les régions et la deuxième, les départements. Les élements des cartes
sont cliquables.
L'utilisateur peut aussi cliquer sur le nom des régions ou des départements, présentés sous la carte,
sous forme de liste.

Pour les communes, l'utilisateur peut cliquer sur leurs noms pour afficher une carte statique.
Les communes sont affichées sous forme de liste avec une pagination.

Toutes cartes sont accompagnées d'un extrait d'article de Wikipédia et d'un lien vers la page de Wikipédia.

L'utilisateur a aussi la possibilité de sauvegarder ses recherches.
L'option de sauvegarde n'est disponible qu'avec la création d'un compte utilisateur.

## Installation et utilisation sur votre ordinateur
Pour utiliser l'application sur votre serveur local:


1. Créez un nouveau projet avec un environnement virtuel puis activez ce dernier.

2. Clonez ce repository:

        git clone https://github.com/Tony380/Projet13.git

3. Installez les dépendances du fichier requirements.txt.

        pip install -r requirements.txt
        
4. Vous aurez besoin de créer une base de données avec postgreSQL nommée 'france'.
Vous pouvez configurer les options qui vous sont personnelles dans le fichier settings.py
dans la partie DATABASE = { }.

5. Toujours dans le fichier settings.py, configurez l'option 'ALLOWED_HOSTS' de la manière suivante:

        ALLOWED_HOSTS = ['*']
        
6. Générez une clé secrète dans la console comme suit:

        $ python
    
        import random, string
    
        "".join([random.choice(string.printable) for _ in range(24)])

7. Gardez cette clé dans vos variables d'environnement en tant que 'SECRET_KEY'.

8. Effectuez les migrations:

        python manage.py makemigrations
        
        python manage.py migrate

9. L'application possède un dump relatif aux tables contenant les coordonnées svg des régions
et des départements pour les cartes. Chargez-le comme ceci:

        python manage.py loaddata maps/dumps/maps.json

10. Enfin, lancez le fichier manage.py en console de cette manière:

        python manage.py runserver


## L'application en ligne
Cette application est aussi utilisable en ligne et est responsive.

Elle est hébergée sur Heroku et utilisable [ici](https://france2020.herokuapp.com "france2020").

## Information complétaire
Le tableau Trello relatif à ce projet se trouve [ici](https://trello.com/b/exMtG38m/projet-13 "Tableau Trello").
