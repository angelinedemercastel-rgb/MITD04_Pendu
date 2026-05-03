# MITD04_Pendu

## Description du projet du Jeu du Pendu

## Langage Python 3.13.7

## Cahier des charges

* Codage d'un jeu du pendu
  * Affichage graphique du pendu de façon dynamique
* Affichage d'un indice sur demande
* Enregistrement et depuis le menu accès aux scores
* Ajout d'un nouveau mot et de son indice
* Affichage des règles du jeu

## Fichiers mots et score

* Les mots sont stockés dans le fichier listeDeMots.txt
  * Structure du fichier de mots :
    [mot],[indice]
* Les scores réalisés sont stockés dans le fichier fichierScore.txt
  * Structure du fichier des scores :
    [date] [heure] [score]

## Jeu du Pendu avec ou sans IHM

On peut jouer de 2 manières :
* En ligne de commande : pendu_cli.py
* Au travers d'une interface homme machine : pendu_code_1.py

## Liste des imports

* tkinter
* random
* datetime
* operation, un fichier contenant des fonctions

## Messages d'erreur

En cas de saisie de plusieurs lettres ou d'un caractère n'appartenant pas à l'alphabet latin,
l'application affiche en rouge le message suivant : "Veuillez saisir une lettre"

## Interface Homme Machine

Image d'une partie : <img width="1180" height="1434" alt="Jeu_en_marche" src="https://github.com/user-attachments/assets/d2a0c080-ee1b-4873-8b83-c2c8a3c1dd0a" />

Image de la page d'acceuil : <img width="1192" height="1446" alt="fenetre_options" src="https://github.com/user-attachments/assets/9cba48d7-87c3-414f-8bf1-dbf050b51b7c" />

Image d'une partie perdue : <img width="1188" height="1448" alt="Partie_perdue" src="https://github.com/user-attachments/assets/4336774a-a5ac-42df-9f04-cae20300fdd2" />


## Auteurs

* Asya YAKUT
* Angéline DEMERCASTEL
* Aiswarya COLLATY
* Samy RAHMANI
