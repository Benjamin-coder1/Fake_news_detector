import compte
import color as c 
import rech 
import data 
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
	try : 
		# we try the algo if an error is found we return 0
		mon_article = rech.Recherche_On_Article(article)
		print("TITLE : ", mon_article.title,'\n')

		# we recover a list of key words usion the stat() function 
		# this function distinguish the type of article (just title / url)
		key_words_li = compte.stat(mon_article)
		print("KEY WORDS : ", key_words_li,'\n')
		
		# Now we make researchs on NewAPI with the key words finded
		m = data.Recherche_NewAPI(key_words_li)

		#Now we have the number of results in m.nb_art
		#We give a note thank to the number of results (see the report)
		note = 1 - exp(-m.nb_art/100)
		nb_m = len(key_words_li)
		if  nb_m < 3 : 
			note += 2*note*(nb_m/3-1)/3
		else :
			note += 2*(1-note)*(nb_m/3-1)/3 


		print(c.Color("------------------------------------------------------------------------","t"))
		print(c.Color("Note 1 : " + str(note),"t"))
		print(c.Color("------------------------------------------------------------------------","t"))
		return note
	except : 
	    # the algo has failed for some possibilities : 
	    #       1- 0 article find on NewAPI
	    #       2- Bad URL 
	    #       3- error with NewAPi   ex : too request in 12h  (max 250) !!!! 
	    print(c.Color("------------------------------------------------------------------------","t"))
	    print(c.Color("An error as happend (bad url/ 0 similar article found/ too NewAPI requests ... )","t"))
	    print(c.Color("Note 1 : 0","t"))
	    print(c.Color("------------------------------------------------------------------------","t"))
	    return 0

scooring_1("https://www.bbc.com/news/world-us-canada-52733220?intlink_from_url=https://www.bbc.com/news/topics/cp7r8vgl2lgt/donald-trump&link_location=live-reporting-story")
