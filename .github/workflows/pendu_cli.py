import random

liste_mots = []

cheminFichier = "./listeDeMots.txt"

def afficheBonjour():
    print("Bonjour ")

def lireChoix():
    print("\n***Bonjour***")
    print("\n[J]ouer au Pendu")
    print("[A]jouter un nouveau mot")
    print("[Q]uitter")
    choix = input("\nChoix : ")
    return choix
