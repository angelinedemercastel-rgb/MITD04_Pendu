from tkinter import *
import operations as op
from PIL import Image, ImageTk


# ---------------- MENU ----------------
'''Fonction : 
        affiche les frame du jeu (donc le score, le canva et la saisie du joueur) 
        et choisi un nouveau mot et remet le score à 7 chances
'''
def ouvrir_jeu():
    frame1.grid()
    frame2.grid()
    frame3.grid()
    nouveauMot()
    afficheScore()


''' Fonction :
        retire les frames
        affiche le menu principal
'''
def retour_menu():
    frame1.grid_remove()
    frame2.grid_remove()
    frame3.grid_remove()
    menu_principal()


''' Fonction :
        créé la fenêtre d'accueil et l'affiche
        avec les boutons (Jouer, Ajouter mot, règles jeu
        scores, quitter
        Avec un image d'arrière plan
'''
def menu_principal():
    global accueil
    accueil = Frame(fen, bg="ivory")
    accueil.place(relwidth=1, relheight=1)

    Label(accueil, text="JEU DU PENDU", font=("Arial", 30), bg="yellow").pack(pady=50)

    Button(accueil, text="Jouer", width=20, height=2,
           command=lambda: [accueil.destroy(), ouvrir_jeu()],bg="yellow").pack(pady=20)

    Button(accueil, text="Ajouter un mot", width=20, height=2,
           command=ajouterMot,bg="yellow").pack(pady=20)

    Button(accueil, text="Règles du jeu", width=20, height=2,
           command=afficheRegles,bg="yellow").pack(pady=20)

    Button(accueil, text="Scores", width=20, height=2,
           command=ouvreFichierScore,bg="yellow").pack(pady=20)

    Button(accueil, text="Quitter", width=20, height=2,
           command=fen.destroy,bg="yellow").pack(pady=20)
    
    global bg_menu_image

    bg_menu = Label(accueil, image=bg_menu_image)
    bg_menu.place(x=0, y=0, relwidth=1, relheight=1)
    bg_menu.lower()
    



# ---------------- JEU ----------------
''' Fonction : 
        Remet l'affichage à zero (réinitialise le pendu)
        remet le fond et la potence
        redessine la potence
        choisi un autre mot 
        remet le score à 7
'''
def rejouer():
    global score
    razAffichage()
    canvas.delete("visage")  # efface la tête
    canvas.create_image(0, 0, image=canvas.bg_canvas, anchor="nw")
    dessinerPotence()
    nouveauMot()
    score = 7


'''
Fonction : validerNouveauMot
        récupère le mot et l'indice de l'utilisateur
        puis vérifie la taille du mot
        si c'est bon : ajouter au fichier Liste de Mots
        puis ferme la fenêtre

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
        Crée une nouvelle fenêtre qui permet au joueur de rentrer
        un nouveau mot avec son indication
        avec un bouton pour valider qui fait appelle à la fonction
        validerNouveauMot
'''
def ajouterMot():
    global eMot, eIndice, page_ouverte
    page_ouverte = Frame(fen)
    page_ouverte.place(x=0, y=0, relwidth=1, relheight=1)

    bg = Label(page_ouverte, image=bg_menu_image)
    bg.place(x=0, y=0, relwidth=1, relheight=1)

    Label(page_ouverte, text="Ajouter un mot", font=("Arial", 30), bg="#A8E6EF").place(relx=0.5, y=80, anchor="center")

    Label(page_ouverte, text="Mot :", font=("Arial", 16), bg="#A8E6EF").place(relx=0.3, y=250, anchor="center")
    eMot = Entry(page_ouverte, width=20, font=("Arial", 16))
    eMot.place(relx=0.6, y=250, anchor="center")

    Label(page_ouverte, text="Indication :", font=("Arial", 16), bg="#A8E6EF").place(relx=0.3, y=350, anchor="center")
    eIndice = Entry(page_ouverte, width=20, font=("Arial", 16))
    eIndice.place(relx=0.6, y=350, anchor="center")

    Button(page_ouverte, text="Valider", width=15, height=2,
           font=("Arial", 14), bg="yellow",
           command=validerNouveauMot).place(relx=0.5, y=470, anchor="center")

    Button(page_ouverte, text="Retour", width=15, height=2,
           font=("Arial", 14), bg="yellow",
           command=page_ouverte.destroy).place(relx=0.5, y=580, anchor="center")



'''
Fonction :
        Choisi aléatoirement un nouveau mot (et son indice)
        qui deviens le mot secret et l'affiche (_)
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
        Vérifie si la case à cocher est cocher 
        si oui : affcihe indice
        si non : n'affiche pas 
'''
def checkCacIndice():
    global indice_mot
    if indiceOn.get() == 1:
        afficheIndice(indice_mot)
    elif indiceOn.get() == 0:
        supprimeIndice()


'''
Fonction :
        affiche le mot secret avec des espaces entre chaque
        lettre qui sont mise en majuscule
'''
def afficheMotSecret():
    lbl_motSecret.config(text=" ".join(mot_secret.upper()))


'''
Fonction :
        Affiche un message d'erreur 
        puis remet la case vide 
'''
def afficheMessageErreur(msgErreur):
    lbl_MessageErreur.config(text=msgErreur)
    razProposition()


'''
Fonction :
        Efface le message d'erreur affiché
'''
def effacerMessageErreur(msgErreur):
    lbl_MessageErreur.config(text=msgErreur)


'''
Fonction :
        Affiche l'indice du mot à deviner
'''
def afficheIndice(indice_mot):
    lbl_indice.config(text=indice_mot)


'''
Fonction :
        si le résultat est "bravo" : le résultat en vert
        si non : le résultat en rouge
'''
def afficheResultat(resultat):
    lbl_resultat.config(text=resultat)
    if "Bravo" in resultat :
        lbl_resultat.config(fg="green")
    else :
        lbl_resultat.config(fg="red")


'''
Fonction :
        Efface le résultat affiché
'''
def effaceResultat(resultat):
    lbl_resultat.config(text=resultat)


'''
Fonction :
        Le label de l'indice est vidé
'''
def supprimeIndice():
    lbl_indice.config(text="")


'''
Fonction :
        Affiche le score actuelle du joueur
'''
def afficheScore():
    lbl_score_value.config(text=str(score))


'''
Fonction :
        Décoche la case indice
'''
def decocheCacIndice():
    cac_indice.deselect()


'''
Fonction :
        Remet à zéro tous les éléments d'affichage
        (score, indice, mot secret, pendu, resultat, saisie du joueur)
        et remet possible la saisie du joueur
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
        remet à zero la zone de saisie
        et ce n'est plus possible de rentrer des lettres
'''
def desactive_entry():
    razProposition()
    ent_saisie.config(state= "disabled")


'''
Fonction :
        remet à zero la zone de saisie
        le joueur peut mettre des lettres
'''
def active_entry():
    razProposition()
    ent_saisie.config(state= "normal")


'''
Fonction :
        vide la zone de saisie
'''
def razProposition():
   ent_saisie.delete(0, END)


'''
Fonction :
        utilisé pour chaque entrée 
        vérifie que la saisie est possible (1 seule lettre)
        vérifie si l'entrée de joueur est dans le mot
        si oui : met à jour le mot secret
        si non : joueur perd 1 point
        puis vérifie si le mot entier est trouvé (plus de _)
        -> affiche la victoire (visage, mot)
        ou si le score est 0 (défaite)
        -> affiche la défaite
        enregistre le score dans le fichier
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
        dessinerVisageContent()
        afficheScore()
        desactive_entry()
        enregistreScore(score)

    if score == 0:
        print("Vous avez perdu !")
        print("Le mot à trouver était : ", mot_a_deviner)
        afficheResultat("Perdu ! Solution : "+mot_a_deviner)
        dessinerVisageTriste()
        desactive_entry()
        enregistreScore(score)

    razProposition()


'''
Fonction :
        déssine la potence sur le canva
        avec le trait de la base, le trait verticale, horizontale, oblique, corde et tête (ovale)
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
    cOvale = canvas.create_oval(xJ, yJ, xK, yK, width=4, outline='black')


'''
Fonction :
        déssine la tête du pendu avec des yeux
'''
def dessinerTete():
    global tete, oeilDroit, oeilGauche
    xJ,yJ, xK, yK = 290,155, 340,205
    tete = canvas.create_oval(xJ, yJ, xK, yK, width=3, fill='pink')
    xJ,yJ, xK, yK = 304,170, 311,180
    oeilDroit = canvas.create_oval(xJ, yJ, xK, yK, width=3, fill='black')
    xJ,yJ, xK, yK = 319,170, 326,180
    oeilGauche = canvas.create_oval(xJ, yJ, xK, yK, width=3, fill='black')


'''Fonction :
        efface le canva, remet le fond
        dessine un visage content (sourire)
'''
def dessinerVisageContent():
    canvas.delete("all")  # efface tout

    canvas.create_image(0, 0, image=canvas.bg_canvas, anchor="nw")

    # tête
    canvas.create_oval(150, 50, 450, 350, fill="pink", outline="black", width=3)

    # yeux
    canvas.create_oval(210, 130, 270, 200, fill="black")
    canvas.create_oval(330, 130, 390, 200, fill="black")

    # sourire
    canvas.create_arc(220, 180, 380, 300, start=200, extent=140, style="arc", width=4)


'''Fonction :
        efface le canva, remet le fond
        dessine un visage triste
'''
def dessinerVisageTriste():
    canvas.delete("all")  # efface tout

    canvas.create_image(0, 0, image=canvas.bg_canvas, anchor="nw")

    # tête
    canvas.create_oval(150, 50, 450, 350, fill="pink", outline="black", width=3)

    # yeux
    canvas.create_oval(210, 130, 270, 200, fill="black")
    canvas.create_oval(330, 130, 390, 200, fill="black")

    # bouche triste
    canvas.create_arc(220, 220, 380, 320, start=20, extent=140, style="arc", width=4)


'''Fonction :
        dessine la bouche du pendu '''
def dessinerBouche():
    global bouche
    xJ,yJ, xK, yK = 310,188, 320,200
    bouche = canvas.create_oval(xJ, yJ, xK, yK, width=3, fill='red')


'''
Fonction :
        dessine le coprs du pendu 
'''
def dessinerTronc():
    global tronc
    xC,yC,xD,yD = 315,206,315,266
    tronc = canvas.create_line(xC, yC, xD, yD, width=3, fill='black')

'''
Fonction :
        dessine la jambe droite du pendu
'''
def dessinerJambeDroite():
    global jambeDroite
    xC,yC,xD,yD = 315,266,270,320
    jambeDroite = canvas.create_line(xC, yC, xD, yD, width=3, fill='black')

'''
Fonction :
        dessine la jambe gauche du pendu
'''
def dessinerJambeGauche():
    global jambeGauche
    xC,yC,xD,yD = 315,266,360,320
    jambeGauche = canvas.create_line(xC, yC, xD, yD, width=3, fill='black')

'''
Fonction :
        dessine le bras gauche du pendu
'''
def dessinerBrasGauche():
    global brasGauche
    xC,yC,xD,yD = 315,216,360,190
    brasGauche = canvas.create_line(xC, yC, xD, yD, width=3, fill='black')

'''
Fonction :
        dessine le bras droit du pendu
'''
def dessinerBrasDroit():
    global brasDroit
    xC,yC,xD,yD = 315,216,270,190
    brasDroit = canvas.create_line(xC, yC, xD, yD, width=3, fill='black')


'''Fonction :
        efface tous les éléments du corps du pendu
        ignore les erreur si un élément du corps n'a pas été dessiné
'''
def effacePendu():
    try :
        canvas.delete(tete)
        canvas.delete(oeilDroit)
        canvas.delete(oeilGauche)
        canvas.delete(bouche)
        canvas.delete(tronc)
        canvas.delete(brasDroit)
        canvas.delete(brasGauche)
        canvas.delete(jambeGauche)
        canvas.delete(jambeDroite)
    except :
        err = "widget inexistant"
        print(err)


'''Fonction :
        crée une nouvelle fenêtre pour afficher les règles du jeu
        tant que cette fenêtre est ouvert, l'utilisateur ne pourra pas jouer
'''
def afficheRegles():
    window = Toplevel(fen)# Création d'une nouvelle fenêtre
    window.title("Règles du jeu")# Définition du titre
    window.geometry("300x200")# Dimensions de la fenêtre

    # Personnalisation de la fenêtre
    window.configure(bg="ivory",relief="raised")# Changement de couleur de fond et du relief

    # Gestion des interactions avec la fenêtre
    window.transient(fen)# Place la fenêtre fille au-dessus de la fenêtre parent
    window.grab_set()# Empêche l'utilisateur d'interagir avec la fenêtre parent
    window.focus_set()# Donne le focus à la fenêtre fille
    label= Label(window, text= "Le but du jeu est simple : \n deviner toute les lettres \n qui doivent composer un mot,\n avec un nombre de tentatives \n limité à 6. \n A chaque fois que le joueur \n devine une lettre, celle-ci est\n affichée. Dans le cas contraire,\n le dessin d’un pendu se met à \n apparaître…", font= ('Aerial', 12))
    label.pack()


'''Fonction : 
        ajoute au fichier du score la date, l'heure et le score d'une partie 
'''
def enregistreScore (score) :
    FichierScore= open("./fichierScore.txt", "a")
    FichierScore.write(op.dateEtHeure() + "   " + str(score) + "\n")
    FichierScore.close()


'''Fonction :
        lit le contenu du fichier des scores
        l'affiche dans une autre fenêtre qui ne peut être changé 
'''
def ouvreFichierScore() :
    FichierScore= open("./fichierScore.txt", encoding="utf-8")
    contenu = FichierScore.read()
    FichierScore.close()

    global page_ouverte
    page_ouverte = Frame(fen)
    page_ouverte.place(x=0, y=0, relwidth=1, relheight=1)

    bg = Label(page_ouverte, image=bg_menu_image)
    bg.place(x=0, y=0, relwidth=1, relheight=1)

    Label(page_ouverte, text="Scores", font=("Arial", 30), bg="#A8E6EF").place(relx=0.5, y=40, anchor="center")

    texte = Text(page_ouverte, width=40, height=15, font=("Arial", 14))
    texte.insert("1.0", contenu)
    texte.config(state="disabled")
    texte.place(relx=0.5, y=300, anchor="center")

    Button(page_ouverte, text="Retour", width=20, height=2,
           font=("Arial", 14), bg="yellow",
           command=page_ouverte.destroy).place(relx=0.5, y=620, anchor="center")



lettreSaisie =""
mot_secret = ""
mot_a_deviner = ""
indice_mot = ""
score=7



#--------------------------------------FENETRE--------------------------------------------------------------
fen = Tk()
image_menu = Image.open("IMG_6422.jpg")
image_menu = image_menu.resize((600, 700))
bg_menu_image = ImageTk.PhotoImage(image_menu)

fen.title('Jeu du Pendu - Mai 2026 - V1.0')
fen.geometry("600x700")

# --- IMAGE DE FOND ---
image_fond = Image.open("IMG_6422.jpg")
image_fond = image_fond.resize((600, 700))  # adapter à la fenêtre
bg_image = ImageTk.PhotoImage(image_fond)

background_label = Label(fen, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


fen.resizable(False, False)

fen.grid_rowconfigure(0,weight=1)
fen.grid_rowconfigure(1,weight=1)
fen.grid_rowconfigure(2,weight=1)
fen.grid_columnconfigure(0,weight=1)
fen.grid_columnconfigure(1,weight=1)
fen.grid_columnconfigure(2,weight=1)

resultat=StringVar()


funcList = []
funcList.append(dessinerJambeDroite)
funcList.append(dessinerJambeGauche)
funcList.append(dessinerBrasGauche)
funcList.append(dessinerBrasDroit)
funcList.append(dessinerTronc)
funcList.append(dessinerBouche)
funcList.append(dessinerTete)

#FRAME 1
frame1 = Frame(fen, bg='ivory',bd=2)
frame1.grid_remove()

lbl_score = Label(frame1, text="Score : ", font="Arial 12",bg='ivory').grid(row=1, column=1,pady=5,padx=5)
lbl_score_value = Label(frame1, text="", font="Arial 12",bg='ivory')
lbl_score_value.grid(row=1, column=2,pady=5,padx=5)

lbl_motATrouver = Label(frame1, text="Mot à trouver : ", font="Arial 12",bg='ivory').grid(row=2, column=1,pady=5,padx=5)

lbl_motSecret = Label(frame1, text="", font="Arial 16",bg='ivory')
lbl_motSecret.grid(row=2, column=2,pady=5,padx=5)
'''lbl_chaine = Label(frame1, text="")
lbl_chaine.grid(row=1, column=2)'''

lbl_resultat = Label(frame1, text="", font="Arial 14",bg='ivory')
lbl_resultat.grid(row=2, column=4)

#FRAME 2
frame2 = Frame(fen, bd=2)
frame2.grid_rowconfigure(0, weight=1)
frame2.grid_columnconfigure(0, weight=1)
frame2.grid_remove()

canvas = Canvas(frame2, width=590, height=380, highlightthickness=0)
canvas.grid(row=0, column=0, sticky="nsew")

# Image de fond directement dans le canvas
bg_canvas = ImageTk.PhotoImage(Image.open("IMG.jpg").resize((590, 380)))
canvas.bg_canvas = bg_canvas
canvas.create_image(0, 0, image=bg_canvas, anchor="nw")


dessinerPotence()

'''canvas.bind("<Button-1>", pointeur)'''
canvas.grid(row=0, column=0, sticky="nsew")

#FRAME 3
frame3 = Frame(fen, bg='ivory',bd=2)
frame3.grid_remove()

indiceOn= IntVar()
cac_indice = Checkbutton(frame3, text = "Indice",
                            height = 2, width = 10, font="Arial 12",bg='ivory',
                            variable=indiceOn,
                            command=checkCacIndice)
cac_indice.grid(row=1, column=0,pady=5,padx=5)

lbl_indice = Label(frame3, text="", font="Arial 12",bg='ivory')
lbl_indice.grid(row=1, column=2,pady=5,padx=5)


lbl_Proposition = Label(frame3, text="Proposition de lettre : ", font="Arial 12",bg='ivory').grid(row=2, column=0,pady=5,padx=5)

ent_saisie = Entry(frame3, width=3, font="Arial 12")
ent_saisie.grid(row=2, column=1,pady=15,padx=5, sticky='w')
ent_saisie.bind("<Return>",traiterLettre)


lbl_MessageErreur = Label(frame3, text="", font="Arial 12",bg='ivory',fg='red')
lbl_MessageErreur.grid(row=2, column=2,pady=5,padx=5)

btn_rejouer = Button(frame3, text="Rejouer",font="Arial 12",bg='ivory',command=rejouer)
btn_rejouer.grid(row=3, column=0,padx=5,pady=10)
btn_quitter_jeu = Button(frame3, text="Quitter le jeu", font="Arial 12", bg='ivory', command=retour_menu)
btn_quitter_jeu.grid(row=3, column=1, padx=5, pady=10)

nouveauMot()
menu_principal()


fen.mainloop()

