import rech
import data 
import trait_lang
import trait_lang
import color as c 
import matplotlib.pyplot as plt 

def scooring_2(article):
    """
    DESCRIPTION 
        this function is the final function of the part 2, it is used in order to give a note to an article 
        in order to see if it is a fake new of not

    PARAMETERS
        param1 : str
            This is either the name of the article, or the url of the article
            FOR BEST RESULT PLEASE USE THE URL  

    OUTPUT  
        out1 : int 
            The note
    """

    # we look for informations creating an instance from param1
    mon_article = rech.Recherche_On_Article(article)
    print(mon_article.title,'\n')

    if hasattr(mon_article,"url") : 
        # if we gave an url we can recover data from the web site 
        # we get a list of list containing the key words
        key_words_li = mon_article.get_combi_key_words()
    else : 
        # else, we have just a title to analyse 
        if len(mon_article.get_key_words_nlp()) != 0 : 
            # We have just a list with the main entities of the sentence
            key_words_li = [mon_article.get_key_words_nlp()]
        else :
            # get_key_words_nlp() didn't find any word
            key_words_li = []

    # we add the all entire title in case of we didn't dinf any key words .... (bad case, you must give an url to avoid that !!)
    key_words_li.append(trait_lang.degrematiser(trait_lang.nettoyer(mon_article.title)).split())
    
    # we store the result of similarity in a list
    list_simi = []
    # we store the title in a list to be sure we don't count some times the same title
    t = []
    for lst in key_words_li : 
        # we send the list of key words to NewAPI and we calculate the similatiry with each title 
        m = data.Recherche_NewAPI(lst)
        for tit in m.title : 
            # m.title contains all the title of the articles find by NewAPI
            if (tit is not None) and (tit not in t)  : 
                t.append(tit)
                print("- ",tit)
                list_simi.append(trait_lang.compare_sentence(tit,mon_article.title))
    print("\n", "number of articles analysed : ", str(len(list_simi)),"\n")
    plt.plot(range(len(list_simi)), [0.85]*len(list_simi))
    plt.plot(range(len(list_simi)), list_simi)
    plt.show()

    return max(list_simi)

print(c.Color("NOTATION : " + str(scooring_2("https://www.bbc.com/news/world-52603017")) ,'v'))



