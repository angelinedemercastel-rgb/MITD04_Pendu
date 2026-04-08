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

def lireListeMots(chemin) :
    print("Chemin", chemin)
    file=open(chemin, "r")
    lignes = file.readlines()
    for ligne in lignes :
        ligne=ligne.strip()
        if ligne :
            parties = ligne.lower().split(",")
            liste_mots.append(parties)
    file.close()
    return liste_mots

def listeIndexLettre(lettre,mot):
    lIndex = []
    for i in range(0,len(mot)):
        if lettre == mot[i]:
            lIndex.append(i)
    return lIndex

def ajouterMot(chemin):
    print("Chemin", chemin)
    file=open(chemin,"a")
    word = input("Mot nouveau : ")
    indication = input("Indication : ")
    s=file.writelines("\n"+word+","+indication)
    file.close()
