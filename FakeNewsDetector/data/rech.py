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
			self.content = urllib.request.urlopen(self.url).read().decode('utf-8')
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
		self.title = self.get_from_to(self.content, "<title>", "</title>")
		print(c.Color("Title recup","t"))

		cont = self.get_from_to(self.content, """<script type="application/ld+json">""", "</script>")
		cont = list(cont)
		for i in range(len(cont)) : 
			if (cont[i] == '\n') : 
				cont[i] = " "

		cont = "".join(cont)
		cont = UserDict(eval(cont))
		if "publisher" in cont.keys() : 
			if type(cont["publisher"]) == dict : 
				self.publisher = cont["publisher"]["name"]
				print(c.Color("publisher  recup","t"))
			else : 
				self.publisher = cont["publisher"]
				print(c.Color("publisher  recup","t"))

		i = 0 
		while self.content[i:(i+len("og:description"))] != "og:description" : 
			i +=1 

		while self.content[i:(i+len("content="))] != "content=" : 
			i +=1 
		i +=9

		self.description = self.content[i:(i+300)]
		print(c.Color("description  recup","t"))




