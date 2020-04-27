import data as d
import rech as r 
from math import exp

import requests
import json 



def compte_mot(liste_mot,mot) : 
	"""compte l'occurence de mot dans liste_chaine_cara"""
	compteur = 0
	for i in liste_mot : 
		if i == mot : 
			compteur += 1

	return compteur

def trier(liste,mot) : 
	# supprime mot de liste_mot 
	liste_bon_mots = []
	for i in range(len(liste)) : 
		if liste[i].upper() != mot.upper() :
			liste_bon_mots.append(liste[i])

	return liste_bon_mots



def stat(mon_article) : 

	useless_word = ['during','while','with','among','more','but','by','First', 'firstly', 'first of all', 'in the first place', 'first and foremost','Secondly','thirdly', 'then', 'next' ,'at first sight', 'as a matter of fact', 'in fact', 'at all events', 'in any cases', 'actually', 'anyway', 'in this respect','to some extent','as far as','from','a', 'to', 'in order to','so as to ','For', 'if' ,'whereas', 'while','unlike', 'contrary to','as against','conversely', 'on the contrary', 'in contrast to','or','else','otherwise','although','though','even','whatever','yet','still','however','nevertheless', 'nonetheless','all','despite', 'in spite of', 'instance','example','such as','like','above all' ,'because','since','thanks','so','that', 'therefore', 'thus','hence','once','well','also','too','similarly','the','a','an','to','from','at','when','for','of','in','and','are','is','would','should','could','have','be','been','will']
	ponct = [':',"'",'«','»','.',',','!','?',';','-',"",'&','0','1','2','3','4','5','6','7','8','9']


	if hasattr(mon_article,'url') : 
		"""on a une URL"""

		titre = list(mon_article.title)

		for pon in ponct : 
			titre = trier(titre,pon).copy()

		titre = "".join(titre).upper().split(" ")
		
		for us_wor in useless_word + ponct : 
			titre = trier(titre,us_wor).copy()


		# algorithme de classement (compliqué ...)
		val_art = {}
		val_int = {}
		val = {}
		i = 0

		for mot in titre : 		
			if mon_article.content.upper().count(mot.upper()) < 500 : 
				val_art[mot] = mon_article.content.upper().count(mot.upper())
				val[mot] = [0,0]
				val_int[mot] = d.Recherche_article([mot.upper()]).nb_art
				print('---' + mot + '---  ', mon_article.content.upper().count(mot.upper()) )


		for i in range(len(val_art)) : 
			a,val_art = max_dict(val_art)
			b,val_int = max_dict(val_int)

			val[a][0] = i + 1
			val[b][1] = i + 1

		for mot in val.keys() :
			val[mot] = 2*val[mot][1] / 3 + val[mot][0] / 3 

		mot = []
		for i in range(len(val)) : 
			a,val = min_dict(val)
			mot.append(a)

	else : 
		"""On a juste un titre"""
		
		titre = list(mon_article.title)

		for pon in ponct : 
			titre = trier(titre,pon).copy()

		titre = "".join(titre).upper().split(" ")
		
		for us_wor in useless_word + ponct : 
			titre = trier(titre,us_wor).copy()


		val_int = {}
		for mot_titre in titre : 
			val_int[mot_titre] = d.Recherche_article([mot_titre.upper()]).nb_art


		mot = []
		for i in range(len(val_int)) : 
			a,val_int = max_dict(val_int)
			mot.append(a)

		return mot 

	if len(mot) <= 6 : 
		return mot 
	else : 
		return mot[0:6]


	

def max_dict(dico) : 
	m = max(dico.values())
	for key,val in dico.items() : 
		if val == m : 
			del dico[key]
			return key,dico

def min_dict(dico) : 
	m = min(dico.values())
	for key,val in dico.items() : 
		if val == m : 
			del dico[key]
			return key,dico

def note(article) : 
	#1- On recupere les infos sur notre article
	print('Notation en cours : ')
	a = r.Recherche(article)
	print(a.title)

	#2- on trie le titre 
	key_words = stat(a)
	print(key_words)

	#3- on fait des Recherche d'article similaires
	m = d.Recherche_article(key_words)

	#4 On donne une note en fonction du nb de résulat et mots clefs
	note = 1 - exp(-m.nb_art/100)
	nb_m = len(key_words)
	if  nb_m < 3 : 
		note += 2*note*(nb_m/3-1)/3
	else :
		note += 2*(1-note)*(nb_m/3-1)/3 
	print('Evaluation : ',note)