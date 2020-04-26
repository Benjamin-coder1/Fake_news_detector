import data as d
import rech as r 

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

	useless_word = ['more','but','by','First', 'firstly', 'first of all', 'not','in the first place', 'first and foremost','Secondly','thirdly', 'then', 'next' ,'at first sight', 'as a matter of fact', 'in fact', 'at all events', 'in any cases', 'actually', 'anyway', 'in this respect','to some extent','as far as','from','a', 'to', 'in order to','so as to ','For', 'if' ,'whereas', 'while','unlike', 'contrary to','as against','conversely', 'on the contrary', 'in contrast to','or','else','otherwise','although','though','even','whatever','yet','still','however','nevertheless', 'nonetheless','all','despite', 'in spite of', 'instance','example','such as','like','above all' ,'because','since','thanks','so','that', 'therefore', 'thus','hence','once','well','also','too','similarly','the','a','an','to','from','at','when','for','of','in','and','are','is','would','should','could','have','be','been','will']
	ponct = [':',"'",'«','»','.',',','!','?',';','-',""]


	if mon_article.publisher in mon_article.title : 
		mon_article.title = mon_article.title[0:-len(mon_article.publisher)]

	titre = list(mon_article.title)


	for pon in ponct : 
		titre = trier(titre,pon).copy()

	titre = "".join(titre).upper().split(" ")
	
	for us_wor in useless_word + ponct : 
		titre = trier(titre,us_wor).copy()

	print(titre)

	val_art = {}
	val_int = {}
	val = {}
	i = 0
	for mot in titre : 
		val[mot] = [0,0]
		val_art[mon_article.content.upper().count(mot.upper())] = mot
		val_int[d.Recherche_article([mot.upper()]).nb_art] = mot
		print('---' + mot + '---  ', mon_article.content.upper().count(mot.upper()) )

	for i in range(len(val_art)) : 
		val[val_int[max(val_int)]][0] = i + 1
		val[val_art[max(val_art)]][1] = i + 1

		del val_int[max(val_int)]
		del val_art[max(val_art)]

	for mot in val.keys() :
		val[mot] = 2*val[mot][1] / 3 + val[mot][0] / 3 

	val = {key:val for val,key in val.items()}
	mot = []


	for i in range(len(val)) : 
		mot.append(val[min(val)])
		del val[min(val)]	
	
	return mot






	





# print(stat("Donald trump"))


