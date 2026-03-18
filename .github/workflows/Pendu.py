import random

Mots = ("python", "algorithme", "suite", "probleme", "etude",  "reel")
'''
tuple temporaire de mots
'''
def indexs(lettre, caractere):
  indexes=[]
  [indexes.append(k) for k, name in enumerate(caractere) if name==lettre]
  return indexes
'''
la fonction cherche tous les indices d'une certaine lettre et les retourne sous forme d'une liste
'''
def remplacer(mot1,ncaractere,index):
 '''
insere le nouveau string "tranches" et l'original
 '''
 return mot1[:index]+ ncaractere+ mot1[index+1:]

def pendu():
  mot = random.choice(Mots)
  essais=6
  '''  
  compte combien d'essais il reste 
  '''
  lettres=[]
  [lettres.append(i) for i in mot if i not in lettres]
  '''
  la liste qui contient toute les lettres dans le mot donner
  '''
  montrer="*"*len(mot)
  '''
   remplace les lettres par des asterisque
  '''

  while True:
    if montrer==mot:
      print("gagner felicitation :)!!!!")
      break
    elif not essais:
      print("oops ressayer :(")
      print("le mot etait:"+ mot)
      break
    '''
  boucle avec une condition d'arret si le joueur a gagner ou si il lui reste plus d'essais 
   '''
    deviner=str(input("Mot : " + montrer + " | Essais restants : " + str(essais) + "\n"))
    if deviner==mot:
      print("gagnant felicitations !!!")
      break
    elif deviner in lettres:
      '''
      si le joueur devine la lettre c'est correct 
      '''
      for i in indexs(deviner, mot):
        montrer=remplacer(montrer, deviner, i)
        '''
        remplace les asterisques avec la bonne lettre 
        '''
    else:
       essais-=1
pendu()
