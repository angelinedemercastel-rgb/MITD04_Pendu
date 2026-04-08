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

def ajouterMot(chemin):
    print("Chemin", chemin)
    file=open(chemin,"a")
    word = input("Mot nouveau : ")
    indication = input("Indication : ")
    s=file.writelines("\n"+word+","+indication)
    file.close()

def ajouterMotIHM(chemin,mot,indication):
    print("Chemin", chemin)
    file=open(chemin,"a")
    s=file.writelines("\n"+mot+","+indication)
    file.close()

def choisirMot():
    mot_a_deviner,indice = random.choice(lireListeMots(cheminFichier))
    return mot_a_deviner,indice

def afficheMotsecret(mot):
    longueurMot = len(mot)
    print("longueur du mot", longueurMot)
    motsecret = ["X" for  in mot]
    return "".join(mot_secret)

def indicesLettre(lettre, mot_a_deviner):
    li = listeIndexLettre(lettre,mot_a_deviner)
    return li
