class NegativeWeight(Exception) : pass
class DemeagementInterdit(Exception): pass
class ErreurInitialisation(Exception): pass

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
		if quantite<=0:
			raise NegativeWeight
		self.poids+=quantite

class Humain(EtreVivant):
		"""docstring for Humain"""
		def __init__(self,age,taille,poids,genre,nom):
			if (type(age)!=int or (hutype(taille)!=float and hutype(taille)!=int)  or (type(poids)!=float and type(poids)!=int) or type(genre)!=str or type(nom)!=str):
				raise ErreurInitialisation
			self.age = age
			self.taille=taille
			self.poids=poids
			self.genre=genre
			self.nom=nom

		def __str__(self):
			return ("je m'appelle "+self.nom+", je suis un(e) "+self.genre)

		def changer_nom(self,nouveau_nom):
			self.nom=nouveau_nom

		def interaction(self):
			print("salut humain")

class Animal(EtreVivant):
	"""Animal ne peux vivre que dans l'eau, l'air ou la terre """
	def __init__(self,age,taille,poids,espece,millieu_de_vie):
		if (type(age)!=int or (type(taille)!=float and type(taille)!= int) or (type(poids)!=float and type(poids)!=int) or type(espece)!=str):
			raise ErreurInitialisation
		if (millieu_de_vie!="eau" and millieu_de_vie!="terre" and millieu_de_vie!="air" ):
			raise ErreurInitialisation
			
		self.age = age
		self.taille=taille
		self.poids=poids
		self.espece = espece
		self.millieu_de_vie=millieu_de_vie

	def __str__(self):
		return "salut ! je suis un(e)"+self.espece 
	
	def demenage(self,nouveau_millieu_de_vie):
		if nouveau_millieu_de_vie!="eau" and nouveau_millieu_de_vie!="air" and nouveau_millieu_de_vie!="terre":
			raise DemeagementInterdit
		self.millieu_de_vie=nouveau_millieu_de_vie
		
	def moyen_deplacement(self):
		if (self.millieu_de_vie=="eau"):
			print("Je me deplace en nagent")
		if (self.millieu_de_vie=="air"):
			print("Je vol super vite")
		else:
			print('Je me déplace en marchant ou en rampant')
