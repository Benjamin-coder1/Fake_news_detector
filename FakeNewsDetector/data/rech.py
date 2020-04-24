import urllib.request 
import error 
import color as c
import traducteur as t



class Recherche : 

	def __init__(self,doc) : 
		if "https://" in doc :
			# on recoit en entrée une url 
			self.url = doc
			self.__content = urllib.request.urlopen(self.url).read().decode('utf-8')
			self.title = self.get_info()
			print(c.Color("Content has been charged it is an URL","g"))

		else : 
			self.title = doc 
			print(c.Color("Content has been charged it is just a title","g"))


	
	@staticmethod
	def get_from_to(contenue,mot1, mot2) : 
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

		"""on recupere d'autre info document """
		cont = self.get_from_to(self.__content, """<script type="application/ld+json">""", "</script>")
	
		if "datePublished" in cont.keys() : 
			self.date_published = cont["datePublished"]
		if "publisher" in cont.keys() : 
			self.source = cont["publisher"]["name"]
		if "headline" in cont.keys() : 
			self.headline = cont["headline"]

	



ma_recherche = Recherche("https://www.bbc.com/news/world-europe-52382196")
ma_recherche.get_info()
print(ma_recherche.title)




