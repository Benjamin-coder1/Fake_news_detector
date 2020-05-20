import data as data
import rech as rech
import requests
import json 
import operator 


# we are goig to five a note to an article only thank to the number or 
# results fin on NewAPI 

def trier(liste,mot) : 
	"""
	DESCRIPTION 
	    this function is use in order to clean a list of a word 

	PARAMETERS
	    param1 : list
	        List of words to clean
	    param2 : list 
	    	list of words to remove from param1

	OUTPUT  
		out1 : list
			param1 without param2
	"""
	for bad_word in mot : 
		while bad_word in liste : 
			liste.remove(bad_word)
	return liste



def stat(mon_article) : 
	"""
	DESCRIPTION 
	    this function is use in order to make statistic of the words of the title 

	PARAMETERS
	    param1 : instance of Recherche_On_Article
	        - it can be from a title (bad)
	        - if can be from an url (the best)  

	OUTPUT  
		out1 : list
			a list with the words with the best occurence 
	"""

	# we start by removing all what is not necessary to the comprehension
	useless_word = ['during','while','with','among','more','but','by','First', 'firstly', 'first of all', 'in the first place', 'first and foremost','Secondly','thirdly', 'then', 'next' ,'at first sight', 'as a matter of fact', 'in fact', 'at all events', 'in any cases', 'actually', 'anyway', 'in this respect','to some extent','as far as','from','a', 'to', 'in order to','so as to ','For', 'if' ,'whereas', 'while','unlike', 'contrary to','as against','conversely', 'on the contrary', 'in contrast to','or','else','otherwise','although','though','even','whatever','yet','still','however','nevertheless', 'nonetheless','all','despite', 'in spite of', 'instance','example','such as','like','above all' ,'because','since','thanks','so','that', 'therefore', 'thus','hence','once','well','also','too','similarly','the','a','an','to','from','at','when','for','of','in','and','are','is','would','should','could','have','be','been','will']
	ponct = [':',"'",'«','»','.',',','!','?',';','-',"",'&','0','1','2','3','4','5','6','7','8','9']

	if hasattr(mon_article,'url') : 
		# first case : we gave an url !

		#--------------- we clean the title -----------------# 
		mon_article.title = "".join(trier(list(mon_article.title),ponct))
		mon_article.title = " ".join(trier(mon_article.title.split(),useless_word))

		#--------------- we class the words -----------------# 
		# we are going to class the words in fuction of their occurence in the text of the article 

		# algorithme de classement (compliqué ...)
		val_art = {}
		val_int = {}
		val = {}
		i = 0

		for mot in mon_article.title.split() : 		
			# for each word in the title we are going to add it on val_art with its occurence
			# for each word in the title we are going to note its importance by the numer of article containing 
			# it on NewAPI 
			val_art[mot] = mon_article.text.upper().count(mot.upper())
			val_int[mot] = data.Recherche_NewAPI([mot.upper()]).nb_art
			val[mot] = [0,0]

		# Know we have 2 dictionnaries with for each word in title its occurence 
		#       1- in the text of the article 
		#		2- in NewAPI 

		for i in range(len(val_art)) : 
			# now we give a note to each article
			# we create a new dictionnary wich associate to each word a list       word:[*,*]
			# this list contain the ranking of the word in fuction of the statistic AND in function of the researchs on the net 

			a = min(val_art.items(), key=operator.itemgetter(1))[0]
			del val_art[a]

			b = min(val_int.items(), key=operator.itemgetter(1))[0]
			del val_int[b]

			val[a][0] = i + 1
			val[b][1] = i + 1

		# we ponder the two notes taking the note by occurences in the text 2 time more important
		for mot in val.keys() :
			val[mot] = 2*val[mot][1] / 3 + val[mot][0] / 3 

		# Now val is a dictionnary containing for each word a note
		# more the note is elevated, more the word is important !
		# So we create now a list withe the words rank by importance 
		mot = []
		for i in range(len(val)) : 
			mot.append(max(val.items(), key=operator.itemgetter(1))[0])
			del val[max(val.items(), key=operator.itemgetter(1))[0]]

	else : 
		#second case : we just have a title 
		
		#--------------- we clean the title -----------------# 
		mon_article.title = "".join(trier(list(mon_article.title),ponct))
		mon_article.title = " ".join(trier(mon_article.title.split(),useless_word))

		#--------------- we class the words -----------------# 
		# we are going to class the words in fuction of their apparition in NewAPI 
		# we put the result in a dictionnary val_int
		val_int = {}
		for mot_titre in mon_article.title.split() : 
			val_int[mot_titre] = data.Recherche_NewAPI([mot_titre.upper()]).nb_art

		# Now val_int is a dictionnary containing for each word the numer of articles containing this word
		# so we are goig to class the words of the title in function of these numer 
		mot = []
		for i in range(len(val_int)) : 
			mot.append(max(val_int.items(), key=operator.itemgetter(1))[0])
			del val_int[max(val_int.items(), key=operator.itemgetter(1))[0]]

	# we return only the first 6 words 
	if len(mot) <= 6 : 
		return mot 
	else : 
		return mot[0:6]


