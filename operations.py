import random
import datetime as dt

liste_mots = []

cheminFichier = "./listeDeMots.txt"
cheminFichierScore = "./fichierScore.txt"


'''Fonction :
        retourne date et heure (jour/mois/année et heure:minutes:secondes)
'''
def dateEtHeure():
    DH = dt.datetime.now()
    return DH.strftime("%d/%m/%y %H:%M:%S")


'''Fonction :
        affiche les actions possible du joueur
        (jouer, ajouter un mot ou quitter)
'''
def lireChoix():
    print("\n***Bonjour***")
    print("\n[J]ouer au Pendu")
    print("[A]jouter un nouveau mot")
    print("[Q]uitter")
    choix = input("\nChoix : ")
    return choix


'''Fonction :
        lit le fichier des mots 
        et renvoie une liste mot, indice 
        avec un retour à la ligne à chaque fois
'''
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


'''Fonction :
        renvoie la liste des indices où la lettre est
'''
def listeIndexLettre(lettre,mot):
    lIndex = []
    for i in range(0,len(mot)):
        if lettre == mot[i]:
            lIndex.append(i)
    return lIndex


'''Fonction :
        ajoute (au fichier des mots) un nouveau mot donné par l'utilisateur 
        avec son indice
'''
def ajouterMot(chemin):
    print("Chemin", chemin)
    file=open(chemin,"a")
    word = input("Mot nouveau : ")
    indication = input("Indication : ")
    s=file.writelines("\n"+word+","+indication)
    file.close()


'''Fonction :
        ajoute (au fichier des mots) un nouveau mot et son indication 
        depuis l'interface graphique
'''
def ajouterMotIHM(chemin,mot,indication):
    print("Chemin", chemin)
    file=open(chemin,"a")
    s=file.writelines("\n"+mot+","+indication)
    file.close()


'''Fonction :
        choisit au hasard un mot avec son indice du fichier de mots 
'''
def choisirMot():
    mot_a_deviner,indice = random.choice(lireListeMots(cheminFichier))
    return mot_a_deviner,indice


'''Fonction :
        Affiche le mot secret sous la forme _ selon sa taille
'''
def afficheMotsecret(mot):
    longueurMot = len(mot)
    print("longueur du mot", longueurMot)
    mot_secret = ["_" for _ in mot]
    return "".join(mot_secret)


'''Fonction : 
        renvoie la liste des indices où la lettre se trouve 
'''
def indicesLettre(lettre, mot_a_deviner):
    li = listeIndexLettre(lettre,mot_a_deviner)
    return li


'''Fonction :
        choisi un mot, met le mot sous forme _
        initialise l score du joueur à 7 
        si le joueur donne une lettre qui ne fait pas parti du mot, décrémente son score
        s'il a 0 -> perdu
        au contraire s'il n'y a plus de _ dans le mot à trouver, il a gagné

'''
def jouer():
    mot_a_deviner,indice = random.choice(lireListeMots(cheminFichier))
    print(mot_a_deviner, indice)

    longueurMot = len(mot_a_deviner)
    print("longueur du mot", longueurMot)
    mot_secret = ["_" for _ in mot_a_deviner]
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

        if "".join(mot_secret).find('_') == -1:
            print("Bravo vous avez trouvé le mot. Votre score est : ",score)
            break

    if score == 0:
        print("Vous avez perdu !")
        print("Le mot à trouver était : ", mot_a_deviner)

    rep = input("Voulez-vous choisir un autre mot ? (O/N) : ")
    if rep == 'N':
        rejouer = False


