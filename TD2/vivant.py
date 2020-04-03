from a import *

#Creation d'un humain
h=Humain("Garcon","Jonas")
h.age=21
h.taille=1.75
h.poids=65
#On joue avec cet humain
print(h)


#Creation d'un animal
a=Animal("vache","terre")
a.age=4
print(a)
a.moyen_deplacement()
a.demenage("air")
print("je demenage de la terre : ")
a.moyen_deplacement()
print ("Trop bien c'est mon anniv :")
a.anniverssaire()
print("J'ai maintenant "+str(a.age)+" ans")


