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

Image d'une partie : <img width="1200" height="1468" alt="Jeu_en_marche" src="https://github.com/user-attachments/assets/ff68eea3-d164-472e-829a-502374961abc" />
Image de la page d'acceuil : <img width="1200" height="1468" alt="fenêtre_options" src="https://github.com/user-attachments/assets/ca09cae2-6d06-4af5-8c62-63b5b171d4b0" />
Image d'une partie gagné : <img width="1184" height="1448" alt="Partie_gagnee" src="https://github.com/user-attachments/assets/dc7b5994-7140-4921-8820-7b739c7cfb15" />

## Auteurs

* Asya YAKUT
* Angéline DEMERCASTEL
* Aiswarya COLLATY
* Samy RAHMANI
