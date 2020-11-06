
import os
#chemin = "/mnt/c/Users/vince/OneDrive/Bureau"
#Change User
chemin = "C:\\Users\\vince\\OneDrive\\Bureau"

def afficherFic(lstRep, largeur):
	for unFic in lstRep:
		print("/".rjust(largeur+1) + unFic)

def afficherRep(entreeRep):
	print(entreeRep[0] + "/")
	afficherFic(entreeRep[2], len(entreeRep[0]))

arbre = os.walk(chemin)
for unRep in arbre:
	afficherRep(unRep)

