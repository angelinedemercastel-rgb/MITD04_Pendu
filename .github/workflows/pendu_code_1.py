from tkinter import *
import operations as op

'''
Fonction : rejouer
Remet chaine vide les chaines de caracteres
Réinitialise l'affichage
Sélectionne un nouveau mot dans la liste
'''
def rejouer():
    global score
    lettreSaisie =""
    mot_secret = ""
    mot_a_deviner = ""
    indice_mot = ""
    razAffichage()
    nouveauMot()
    score=7
'''
Fonction : validerNouveauMot
'''
def validerNouveauMot():
    mot=eMot.get()
    #print(mot)
    indice=eIndice.get()
    #print(indice)
    if len(mot)!=0 :
        op.ajouterMotIHM(op.cheminFichier,mot,indice)
    fenetreAddWord.destroy()

