import urllib.request 
import error 
import color as c
import traducteur as t

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
			self.title = self.get_title()
			print(c.Color("Content has been charged it is an URL","g"))

		else : 
			self.title = doc 
			print(c.Color("Content has been charged it is just a title","g"))


	@staticmethod 
	def nettoyage_caracteres_speciaux(chaine) : 
		caract_speciaux = {"&#x27;":"'" }
		for car in caract_speciaux.keys() :
			if car in chaine : 
				car1 = car
				chaine = list(chaine) 
				car = list(car)
				for i in range(len(chaine)-len(car)+1) : 
					if chaine[i:(i+len(car))] == car :
						for k in range(i,(i+len(car))) :  
							chaine[k] = "" 
						chaine[i] = caract_speciaux[car1]
				chaine = "".join(chaine)
		return chaine

	def get_title(self) :
		"""on recupere le titre du document """
		j = 0
		deb = 0
		fin = 0
		mot1 = "<title>"
		mot2 = "</title>"
		while fin == 0 and j < (len(self.__content)+len(mot1) + len(mot2)) : 
			if self.__content[j:(j+len(mot1))] == mot1 : 
				deb = j
			if self.__content[j:(j+len(mot2))] == mot2 : 
				fin = j
			j +=1
		if deb == fin : 
			raise error.BadUrl
		return self.nettoyage_caracteres_speciaux(self.__content[(deb+len(mot1)):fin])

	


url_liste = ["https://www.lefigaro.fr/politique/coronavirus-castaner-previent-que-le-deconfinement-ne-signifiera-pas-la-liberte-d-aller-partout-20200423",
"https://www.lefigaro.fr/actualite-france/on-s-est-dit-ca-suffit-on-arrete-quand-le-couple-subit-la-loi-du-confinement-20200423",
"https://edition.cnn.com/2020/04/23/health/coronavirus-vaccine-trial-uk-gbr-intl/index.html"]


for url in url_liste : 
	ma_recherche = Recherche(url)
	print(ma_recherche.title)





