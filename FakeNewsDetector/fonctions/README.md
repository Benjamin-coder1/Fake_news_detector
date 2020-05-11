Cette partie est consacrée a récuperer les données et les stocker pour la suite
ATTENTION pour la compilation vérifier que c'est bien python3 et pas une version anterieur (erreur avec le module color sinon)
Elle comporte pour l'instant 3 modules : 

error.py : 
	ce module a pour but de gérer les differentes erreurs dans la prise en charge des donnes 

data.py : 
	Ce module recupere les données depuis NewsAPI
	On construit une classe dans laquelle on stocke la recherche 

color.py : 
	Ce module est facultatif, il permet simplement de mettre un peu de couleur dans le terminal afin de rendre les resulats plus en evidence 

traducteur.py (Yandex Translate) : 
	Ce module permet de traduire des mots/phrase, il n'est pas encore certain qu'il servira dans la suite cependant il permettrait un eventuel élargissement des sources et améliorerait la fiabilité ! 

	lien recupérer clef : https://translate.yandex.com/developers/keys
	lien doc : https://tech.yandex.com/translate/doc/dg/reference/translate-docpage/

rech.py : 
	Ce module sert a a recuperer une URL et a creer un objet a partir de cet url qui sera le point de depart du travail pour la notation, Pour l'instant une instance ne contient que le titre mais d'autres informations pouraient bien etre récupérées si besoin 
	
Compte.py : 
	Ce module sert a la notation de l'article, il contient des programmes traitant l'article en recuperant les informations grace aux modules précédent puis il note la validité de l'article selon ses recherches
	NOTONS bien que malgres tout les résulats affichés ne sont que tres approximatifs voir tres souvent meme faux, cela est du a la facon d'évaluer les données, de simples données statistiques sans comprehension du sens ont peu de valeurs

Pour lancer le programme aller dans compte.py puis taper :
	co.note(article_titre/article_url)