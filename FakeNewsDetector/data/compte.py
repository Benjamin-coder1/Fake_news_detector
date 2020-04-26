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



def get_syn(mot) : 
	"""donne les synonymes de mot"""
	app_id = "8cbbf6fa"
	app_key = "e66a1dd040c7a05afc372f189c66c98c"
	url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/en-gb/" + mot.lower()
	r = requests.get(url, headers={"app_id":app_id, "app_key":app_key}).json()

	syn_mot = []
	if len(r) == 1 : 
		return []

	for k in r['results'][0]['lexicalEntries'] : 
		if 'synonyms' in k['entries'][0]['senses'][0].keys() : 
			for i in k['entries'][0]['senses'][0]['synonyms'] :
				syn_mot.append(i['text'])

	return syn_mot

def key_words(article) : 
	"""determine les mots clefs"""
	titre = article['title']
	titre = titre.upper().split()

	descr = article['description']
	descr = descr.upper().split()

	useless_word = ['by','First', 'firstly', 'first of all', 'in the first place', 'first and foremost','Secondly','thirdly', 'then', 'next' ,'at first sight', 'as a matter of fact', 'in fact', 'at all events', 'in any cases', 'actually', 'anyway', 'in this respect','to some extent','as far as','from','a', 'to', 'in order to','so as to ','For', 'if' ,'whereas', 'while','unlike', 'contrary to','as against','conversely', 'on the contrary', 'in contrast to','or','else','otherwise','although','though','even','whatever','yet','still','however','nevertheless', 'nonetheless','all','despite', 'in spite of', 'instance','example','such as','like','above all' ,'because','since','thanks','so','that', 'therefore', 'thus','hence','once','well','also','too','similarly','the','a','an','to','from','at','when','for','of','in','and','are','is','would','should','could','have','be','been','will']
	ponct = [':',"'",'«','»','.',',','!','?',';','-']

	for us_wor in useless_word + ponct : 
		descr = trier(descr,us_wor).copy()
		titre = trier(titre,us_wor).copy()

	print(titre)
	print(descr)
	print('\n')

	liste_mot_clefs = []
	for mot in descr : 
		print('---' + mot + '---')
		syn_mot = get_syn(mot)
		for syn in syn_mot + [mot]: 
			print('*' + syn)
			if syn.upper() in titre : 
				if syn.upper() not in liste_mot_clefs : 
					liste_mot_clefs.append(syn.upper())

	print(liste_mot_clefs)
	# en théorie on a ou pas une liste de mot clefs reste a voir si elle est vide ou non 

	return liste_mot_clefs







# print(stat("Donald trump"))


