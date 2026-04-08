from tkinter import *

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

'''
Fonction :
'''
def dessinerBrasGauche():
    global brasGauche
    xC,yC,xD,yD = 315,216,360,190
    brasGauche = canvas.create_line(xC, yC, xD, yD, width=3, fill='black')

'''
Fonction :
'''
def dessinerBrasDroit():
    global brasDroit
    xC,yC,xD,yD = 315,216,270,190
    brasDroit = canvas.create_line(xC, yC, xD, yD, width=3, fill='black')


fen = Tk()
fen.title('Jeu du Pendu - Mai 2025 - V1.0')
fen.geometry("600x700")
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
... (36lignes restantes)
