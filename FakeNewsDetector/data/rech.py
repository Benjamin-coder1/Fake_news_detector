import urllib.request 
import error 
import color as c
import traducteur as t
from collections import UserDict


class Recherche : 

	def __init__(self,doc) : 
		"""Cette classe permet de stocker les valeurs de l'information que l'on analyse"""
		if "https://" in doc :
			# on recoit en entrée une url 
			self.url = doc
			self.__content = urllib.request.urlopen(self.url).read().decode('utf-8')
			print(c.Color("Content has been charged it is an URL","g"))
			self.get_info() #on recupere le plus d'info nécessaire possible 

		else : 
			# On recoit un titre en entrée
			self.title = doc 
			print(c.Color("Content has been charged it is just a title","g"))


	
	@staticmethod
	def get_from_to(contenue,mot1, mot2) : 
		"""recupere le contenue entre mot1 et mot2 dans contenue"""
		j = 0
		deb = 0
		fin = 0
		while (fin == 0) and (j < (len(contenue)+len(mot1) + len(mot2))) : 
			if contenue[j:(j+len(mot1))] == mot1 : 
				deb = j
			if (contenue[j:(j+len(mot2))] == mot2) and (deb != 0): 
				fin = j
			j +=1
		if deb == fin : 
			raise error.BadUrl
		return contenue[(deb+len(mot1)):fin]

	def get_info(self) :
		"""on recupere le titre du document """
		self.title = self.get_from_to(self.__content, "<title>", "</title>")
		print(c.Color("Title recup","t"))
		"""on recupere d'autre info document """
		cont = self.get_from_to(self.__content, """<script type="application/ld+json">""", "</script>")
		# etonament on ne peux faire de cont un dictionnaire sans supprimer le caractere \n qui pose probleme 
		# On l'élimine donc 
		cont = list(cont)
		for i in range(len(cont)) : 
			if (cont[i] == '\n') : 
				cont[i] = " "
		cont = "".join(cont)
		cont = UserDict(eval(cont))
		# On recupere, si cela est possible le plus d'informations necessaires possibles
		# On les sauvegarde dans des attributs
		if "datePublished" in cont.keys() : 
			self.date_published = cont["datePublished"]
			print(c.Color("date publication recup","t"))
		if "publisher" in cont.keys() : 
			self.publisher = cont["publisher"]["name"]
			print(c.Color("publisher  recup","t"))
		if "headline" in cont.keys() : 
			self.headline = cont["headline"]
			print(c.Color("headline recup","t"))
		if "@type" in cont.keys() : 
			self.type = cont["@type"]
			print(c.Color("type recup","t"))

	



# ma_recherche = Recherche("https://www.bbc.com/news/world-us-canada-52407177")
# print(ma_recherche.title)
