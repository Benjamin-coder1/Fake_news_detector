#Ce module permet de traduire dans differentes langues 
import requests
import error
import color as c 


def traduction(phrase_a_traduire,langue_depart,langue_finale,a=0) : 
	"""on donne en entree une phase a traduire, les langues et un parametre non oblagatoire pour afficher ou non le resulat"""
	if (langue_finale not in ['ar','de','en','es','fr','he','it','nl','no','pt','ru','se','ud','zh']) or (langue_depart not in ['ar','de','en','es','fr','he','it','nl','no','pt','ru','se','ud','zh']) : 
		raise error.BAdLanguage

	API_Key = "trnsl.1.1.20200421T100012Z.6fdad5b13cfe475e.d371c4b71ecf82b3f1fa7879c4433d66dc45fbef"
	url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
	url += '?key=' + API_Key + '&text=' + phrase_a_traduire + '&lang=' + langue_depart + '-' + langue_finale
	reponse = requests.get(url).json()

	if a == 1 :
		"""si l'on veut afficher le resulats"""
		print(c.Color(langue_depart.upper() + " : "  + phrase_a_traduire,"t"))
		print(c.Color(langue_finale.upper() + " : "  + reponse['text'][0],"t"))

	return reponse['text'][0]

