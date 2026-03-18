import random

Mots = ("python", "algorithme", "suite", "probleme", "etude",  "reel")
  #tuple temporaire de mots

def indexs(lettre, caractere):
  indexes=[]
  [indexes.append(k) for k, name in enumerate(caractere) if name==lettre]
  return indexes
#la fonction cherche tous les indices d'une certaine lettre et les retourne sous forme d'une liste

def remplacer(mot1,ncaractere,index):
  #insere le nouveau string "tranches" et l'original
  return mot1[:index]+ ncaractere+ mot1[index+1:]
