import fonctions.compte as compte
import fonctions.color as c
import fonctions.rech as rech
import fonctions.data as d
from math import exp

# Ce module permet de lancer le programme fait pour la partie 1 sans nlp



def scooring_1(article) : 
	"""
	DESCRIPTION 
	    this function is the final function of the part 1, it is used in order to give a note to an article 
	    in order to see if it is a fake new of not

	PARAMETERS
	    param1 : str
	        This is either the name of the article, or the url of the article
	        FOR BEST RESULT PLEASE USE THE URL  

	OUTPUT  
	    out1 : int 
	        note
	"""

	# we look for informations creating an instance from param1
	mon_article = rech.Recherche_On_Article(article)
	print(mon_article.title,'\n')

	# we recover a list of key words usion the stat() function 
	# this function distinguish the type of article (just title / url)
	key_words_li = compte.stat(mon_article)
	print(key_words_li)
	
	# Now we make researchs on NewAPI with the key words finded
	m = d.Recherche_NewAPI(key_words_li)

	#Now we have the number of results in m.nb_art
	#We give a note thank to the number of results (see the report)
	note = 1 - exp(-m.nb_art/100)
	nb_m = len(key_words_li)
	if  nb_m < 3 : 
		note += 2*note*(nb_m/3-1)/3
	else :
		note += 2*(1-note)*(nb_m/3-1)/3 
	return note

print(c.Color("NOTATION : " + str(scooring_1("https://www.bbc.com/news/world-52603017")) ,'v'))
