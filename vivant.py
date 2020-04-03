class EtreVivant():
	"""docstring for EtreVivant"""
	def __init__(self,age,taille,poids):
		self.age = age
		self.taille=taille
		self.poids=poids

	def __str__(self):
		print("j'ai "+age+" ans, je paise "+poids+" kg et je mesure "+taille+"m")
	
	def anniverssaire(self):
		self.age+=1

	def manger(self,quantite):
		self.poids+=quantite

class Humain(EtreVivant):
		"""docstring for Humain"""
		def __init__(self,genre,nom):
			self.genre=genre
			self.nom=nom

		def __str__(self):
			return ("je m'appelle "+self.nom+", je suis un(e) "+self.genre)

		def changer_nom(self,nouveau_nom):
			self.nom=nouveau_nom

		def interaction(self):
			print("salut humain")

class Animal(EtreVivant):
	"""docstring for Animal"""
	def __init__(self, espece,millieu_de_vie):
		self.espece = espece
		self.millieu_de_vie=millieu_de_vie

	def __str__(self):
		return "salut ! je suis un(e)"+self.espece 
	
	def demenage(self,nouveau_millieu_de_vie):
		self.millieu_de_vie=nouveau_millieu_de_vie
		
	def moyen_deplacement(self):
		if (self.millieu_de_vie=="eau"):
			print("Je me deplace en nagent")
		if (self.millieu_de_vie=="air"):
			print("Je vol super vite")
		else:
			print('Je me deplace en marchant ou en rampant')

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


