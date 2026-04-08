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

def jouer():
    mot_a_deviner,indice = random.choice(lireListeMots(cheminFichier))
    print(mot_a_deviner, indice)

    longueurMot = len(mot_a_deviner)
    print("longueur du mot", longueurMot)
    mot_secret = ["*" for _ in mot_a_deviner]
    print("".join(mot_secret))

    score = 7
    while score > 0:
        lettre = input("Proposez une lettre : ").lower()
        print(lettre)

        li = listeIndexLettre(lettre,mot_a_deviner)
        #print(li)
        if len(li)==0:
            score=score-1
            print("score : ", score)
        else :
            for i in li:
                mot_secret[i] = lettre
                print("".join(mot_secret))

        if "".join(mot_secret).find('*') == -1:
            print("Bravo vous avez trouvé le mot. Votre score est : ",score)
            break

    if score == 0:
        print("Vous avez perdu !")
        print("Le mot à trouver était : ", mot_a_deviner)

    rep = input("Voulez-vous choisir un autre mot ? (O/N) : ")
    if rep == 'N':
        rejouer = False


