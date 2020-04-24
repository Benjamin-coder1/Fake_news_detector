import data as d
import rech as r 


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


def valider(article,mot_clef) : 
	useless_word = ['le','la','les','de','des','du','un','une','ou','que','quoi']
	ponct = [':',"'",'«','»','.',',','!','?',';']

	if (article['title'] is None) or ( article['content'] is None) or ( article['description'] is None) : 
		return 0,1

	if ("".join(mot_clef) in article['title']) or ("".join(mot_clef) in article['content']) or ("".join(mot_clef) in article['description']) :
		return 1,0

	c = 0 # nombre doccurence totale des mots clefs dans la description de l'article 

	b = article['title'].upper().split()
	for us_wor in useless_word + ponct : 
		b = trier(b,us_wor).copy()


	for mot in mot_clef : 
		c += compte_mot(b,mot.upper())

	b = article['content'].upper().split()
	for mot in mot_clef : 
		c += compte_mot(b,mot.upper())

	b = article['description'].upper().split()
	for mot in mot_clef : 
		c += compte_mot(b,mot.upper())

	# pifometre	
	print(c)
	if c > len(mot_clef)/5 : 
		return 1,0
	return 0,0


def stat(mon_url) : 
	mon_article = r.Recherche(mon_url)    #article qu'on vux analyser
	les_articles = d.Recherche_article(mon_article.title.split(),[],[],0,0,["en"])
	les_articles.url_everything()
	les_articles.get_data()

	cte = 0
	bon_article = 0

	if len(les_articles.result) == 0 : 
		return 0
	for article in les_articles.result :
		a,b = valider(article,mon_article.title.split())
		bon_article += a
		cte += b
		print("-------", bon_article,"-------")

	print(bon_article * 100 / (len(les_articles.result) - cte))	

# print(stat("Donald trump"))


