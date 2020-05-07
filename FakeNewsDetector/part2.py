import rech
import data 
import trait_lang
#article correspond à ce l'utilisateur a ecrit dans la barre de recherche
def scooring(article):
    #mon_article est un object qui contient le titre si article est un titre 
    #mon_article est un object qui contient l'ensemble des infos de l'article si article est une url
    mon_article=rech.Recherche(article)
    #KeyWord permet d'extraire les mots cles de mon_article
    mots_cles=mon_article.KeyWord()
    #On recherche les articles contenants les mots cles dans news api
    all_article=data.Recherche_article(mots_cles)
    titles=all_article.title
    results=[]  
    for elt in title:
        results.append(trait_lang.compare_sentence(elt,mon_article.title))
    return max(results)*100 
