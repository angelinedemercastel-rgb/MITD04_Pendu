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
'''
Fonction :
'''
def ajouterMot():
    global eMot, eIndice,fenetreAddWord
    fenetreAddWord = Toplevel(fen)
    fenetreAddWord.geometry("250x100")
    fenetreAddWord.title("Ajout mot")
    fenetreAddWord.resizable(False, False)
    txt1 = Label(fenetreAddWord, text = 'Mot :')
    txt2 = Label(fenetreAddWord, text = 'Indication :')
    buttonValidationNouveauMot = Button(fenetreAddWord, text="Valider", command=validerNouveauMot)
    eMot = Entry(fenetreAddWord)
    eIndice = Entry(fenetreAddWord)
    txt1.grid(row =0, column =1,pady=5,padx=5)
    txt2.grid(row =1, column =1,pady=5,padx=5)
    eMot.grid(row =0, column =2,pady=5,padx=5)
    eIndice.grid(row =1, column =2,pady=5,padx=5)
    buttonValidationNouveauMot.grid(row =3, column =1,columnspan=2, pady=5,padx=5)

'''
Fonction :
'''
def nouveauMot():
    global mot_a_deviner
    global indice_mot
    global mot_secret
    mot_a_deviner,indice_mot = op.choisirMot()
    #print(mot_a_deviner,indice_mot)
    mot_secret = op.afficheMotsecret(mot_a_deviner)
    #print(mot_secret)
    afficheMotSecret()

'''
Fonction :
'''
def checkCacIndice():
    global indice_mot
    if indiceOn.get() == 1:
        afficheIndice(indice_mot)
    elif indiceOn.get() == 0:
        supprimeIndice()

'''
Fonction :
'''
def afficheMotSecret():
    lbl_motSecret.config(text=" ".join(mot_secret.upper()))

'''
Fonction :
'''
def afficheMessageErreur(msgErreur):
    lbl_MessageErreur.config(text=msgErreur)
    razProposition()

'''
Fonction :
'''
def effacerMessageErreur(msgErreur):
    lbl_MessageErreur.config(text=msgErreur)
'''
Fonction :
'''
def afficheIndice(indice_mot):
    lbl_indice.config(text=indice_mot)

'''

'''
def afficheResultat(resultat):
    lbl_resultat.config(text=resultat)
    if "Bravo" in resultat :
        lbl_resultat.config(fg="green")
    else :
        lbl_resultat.config(fg="red")
'''

'''
def effaceResultat(resultat):
    lbl_resultat.config(text=resultat)

'''
Fonction :

'''
def supprimeIndice():
    lbl_indice.config(text="")

'''
Fonction :

'''
def afficheScore():
    lbl_score_value.config(text=str(score))

'''
Fonction :

'''
def decocheCacIndice():
    cac_indice.deselect()

'''
Fonction :

'''
def razAffichage():
    lbl_score_value.config(text="")
    lbl_indice.config(text="")
    decocheCacIndice()
    lbl_motSecret.config(text="")
    razProposition()
    active_entry()
    effacePendu()
    lbl_resultat.config(text="")

'''
Fonction :

'''
def desactive_entry():
    razProposition()
    ent_saisie.config(state= "disabled")

'''
Fonction :

'''
def active_entry():
    razProposition()
    ent_saisie.config(state= "normal")

'''
Fonction :

'''
def razProposition():
   ent_saisie.delete(0, END)

'''
Fonction :
'''
def traiterLettre(event):
    global listeIndice, score, mot_secret
    effacerMessageErreur("")
    if score == 0:
        return
    lettreSaisie = str(ent_saisie.get())
    if len(lettreSaisie)!= 1 or not lettreSaisie.isalpha() :
        afficheMessageErreur("Veuiller saisir une lettre")
        return
    lettreSaisie = lettreSaisie.lower()
    print(lettreSaisie)
    listeIndice = op.indicesLettre(lettreSaisie,mot_a_deviner)
    #print(listeIndice)
    if len(listeIndice)==0:
        score=score-1
        print("score : ", score)
        afficheScore()
        funcList[score]()
    else :
        for i in listeIndice:
            mot_secret = mot_secret[:i] + lettreSaisie + mot_secret[i+1:]
            #print("".join(mot_secret))
        afficheMotSecret()
    if "".join(mot_secret).find('_') == -1:
        print("Bravo vous avez trouvé le mot. Votre score est : ",score)
        afficheResultat("Bravo !")
        afficheScore()
        desactive_entry()
        enregistreScore(score)

    if score == 0:
        print("Vous avez perdu !")
        print("Le mot à trouver était : ", mot_a_deviner)
        afficheResultat("Perdu ! Solution : "+mot_a_deviner)
        desactive_entry()
        enregistreScore(score)

    razProposition()

'''
Fonction :

'''
def dessinerPotence():
    #A(250,600) B(300,600) C(275,600) D(,) E(,) F(,) G(,)
    global xA,yA,xB,yB
    xA,yA,xB,yB = 130,355,250,355
    xC,yC,xD,yD = 190,355,190,100
    xE,yE,xG,yG = 350,100,272,100
    xF,yF, xH, yH = 185,200, 315,100
    xI, yI = 315, 155
    xJ,yJ, xK, yK = 295,155, 335,205
    global cBaseAB, cVerticaleCD, cHonritaleDE, cObliqueFG, cOvale
    cBaseAB = canvas.create_line(xA, yA, xB, yB, width=8, fill='black')
    cVerticaleCD = canvas.create_line(xC, yC, xD, yD, width=8, fill='black')
    cHonritaleDE = canvas.create_line(xD-10, yD, xE, yE, width=8, fill='black')
    cObliqueFG = canvas.create_line(xF, yF, xG, yG, width=8, fill='black')
    cCordeHI = canvas.create_line(xH, yH, xI, yI, width=4, fill='black')
    cOvale = canvas.create_oval(xJ, yJ, xK, yK, width=4, fill='ivory')

'''
Fonction :
'''
def dessinerTete():
    global tete, oeilDroit, oeilGauche
    xJ,yJ, xK, yK = 290,155, 340,205
    tete = canvas.create_oval(xJ, yJ, xK, yK, width=3, fill='ivory')
    xJ,yJ, xK, yK = 304,170, 311,180
    oeilDroit = canvas.create_oval(xJ, yJ, xK, yK, width=3, fill='ivory')
    xJ,yJ, xK, yK = 319,170, 326,180
    oeilGauche = canvas.create_oval(xJ, yJ, xK, yK, width=3, fill='ivory')

def dessinerBouche():
    global bouche
    xJ,yJ, xK, yK = 310,188, 320,200
    bouche = canvas.create_oval(xJ, yJ, xK, yK, width=3, fill='ivory')


'''
Fonction :
'''
def dessinerTronc():
    global tronc
    xC,yC,xD,yD = 315,206,315,266
    tronc = canvas.create_line(xC, yC, xD, yD, width=3, fill='black')

'''
Fonction :
'''
def dessinerJambeDroite():
    global jambeDroite
    xC,yC,xD,yD = 315,266,270,320
    jambeDroite = canvas.create_line(xC, yC, xD, yD, width=3, fill='black')

'''
Fonction :
'''
def dessinerJambeGauche():
    global jambeGauche
    xC,yC,xD,yD = 315,266,360,320
    jambeGauche = canvas.create_line(xC, yC, xD, yD, width=3, fill='black')

