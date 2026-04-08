import random
import datetime as dt

liste_mots = []

cheminFichier = "./listeDeMots.txt"
cheminFichierScore = "./fichierScore.txt"


def dateEtHeure():
    DH = dt.datetime.now()
    return DH.strftime("%d/%m/%y %H:%M:%S")


def lireChoix():
    print("\n***Bonjour***")
    print("\n[J]ouer au Pendu")
    print("[A]jouter un nouveau mot")
    print("[Q]uitter")
    choix = input("\nChoix : ")
    return choix

def lireListeMots(chemin) :
    print("Chemin", chemin)
    file=open(chemin, "r", encoding="cp1252")
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
