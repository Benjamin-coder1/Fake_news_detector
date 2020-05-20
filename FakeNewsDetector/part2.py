import rech 
import data 
import trait_lang 
import error 
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

    try : 
        # we look for informations creating an instance from param1
        mon_article = rech.Recherche_On_Article(article)
        print("TITLE : ", mon_article.title,'\n')

        if hasattr(mon_article,"url") : 
            # if we gave an url we can recover data from the web site 
            # we get a list of list containing the key words
            key_words_li = mon_article.get_combi_key_words()
        else : 
            # else, we have just a title to analyse 
            key_words_li = [mon_article.get_key_words_nlp()]
            
        # we add the all entire title in case of we didn't find any key words .... (bad case, you must give an url to avoid that !!)
        key_words_li.append(trait_lang.degrematiser(trait_lang.nettoyer(mon_article.title)).split())
        while [] in key_words_li : 
            key_words_li.remove([])

        print("KEY WORDS : ", key_words_li)
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
        print("\nNUMBER OF ARTICLES ANALYSED : ", str(len(list_simi)),"\n")
        ma = max(list_simi)
        #plt.plot(range(len(list_simi)), [0.85]*len(list_simi))
        #plt.plot(range(len(list_simi)), list_simi)
        #plt.show()
        print(c.Color("------------------------------------------------------------------------","t"))
        print(c.Color("Note 2 : " + str(ma),"t"))
        print(c.Color("------------------------------------------------------------------------","t"))
        return ma

    except : 
        # the algo has failed for some possibilities : 
        #       1- 0 article find on NewAPI
        #       2- Bad URL 
        #       3- error with NewAPi   ex : too request in 12h  (max 250) !!!! 
        print(c.Color("------------------------------------------------------------------------","t"))
        print(c.Color("An error as happend (bad url/ 0 similar article found/ too NewAPI requests ... )","t"))
        print(c.Color("Note 2 : 0","t"))
        print(c.Color("------------------------------------------------------------------------","t"))
        return 0


scooring_2("https://www.bbc.com/news/world-us-canada-52733220?intlink_from_url=https://www.bbc.com/news/topics/cp7r8vgl2lgt/donald-trump&link_location=live-reporting-story")