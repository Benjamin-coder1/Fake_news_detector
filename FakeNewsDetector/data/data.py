
import requests
import error 
import color as c 


class Recherche_article : 

    def __init__(self,key_word,key_word_in_title,sources,from_date,to_date,langage) : 
        if (type(key_word) != list) or (type(key_word_in_title) != list) or (type(sources) != list) or (type(langage) != list):
            """on veut enfait des liste contenant les valeur que l'on veut"""
            raise error.BadDictio
   
        if (type(from_date) != int ) or (type(to_date) != int) :
            """on veut des dates au format int bien évidement """
            raise error.BadDictio

        for val in key_word + key_word_in_title + sources + langage  : 
            """on verifie que l'on a bien donné des mots"""
            if type(val) != str :
                raise error.BadDictio

        for val in langage : 
            """ le langage ne peut etre que ceux dessous"""
            if val not in  ['ar','de','en','es','fr','he','it','nl','no','pt','ru','se','ud','zh'] : 
                raise error.BadDictio

        if from_date > to_date :
            """les dates doivent aller correctement""" 
            raise error.BadDictio

        self.key_word = key_word
        self.key_word_in_title = key_word_in_title
        self.sources = sources
        self.from_date = from_date
        self.to_date = to_date
        self.langage = langage
        self.sortby = 'revelancy' 
        self.url = ''


    @staticmethod
    def affiche(url,sep,list_mot,mot_init) : 
        """cette fonction sert pour les 2 fonctions suivantes afin de generer l'URL en respectant les consignes 
        trouvées sur le site NewsAPI"""
        if len(list_mot) != 0 : 
            url += mot_init
            i = 1
            for val in list_mot : 
                if i == len(list_mot) :
                    url += val 
                else : 
                    url += val + sep
                i += 1
        return url 
        

    
    def url_everything(self) : 
        """on va générer une URL pour everything grace aux attribut de recherche"""
        self.url = 'https://newsapi.org/v2/everything?'

        self.url = self.affiche(self.url,'+',self.key_word,"q=")
        self.url = self.affiche(self.url,'+',self.key_word_in_title,"&qInTitle=")
        self.url = self.affiche(self.url,',',self.sources,"&sources=")
        self.url = self.affiche(self.url,'&language=',self.key_word_in_title,"&language=")

        self.url += '&sortBy=' + self.sortby + '&'
        if self.from_date != 0  :
            self.url += 'from=' + str(self.from_date) + '-00-00&'
        if self.to_date != 0 :
            self.url += 'to=' + str(self.to_date) + '-12-30&'
        self.url += 'apiKey=41ff73330072433da7a7f9b8171e5989'
        print(c.Color("The URL has been sucefully created ! ","g"))
        return self.url

    def url_top_headlines(self) : 
        """on va générer une URL pour everything grace au attribut de recherche"""
        self.url = 'https://newsapi.org/v2/top-headlines?'

        self.url = self.affiche(self.url,'+',self.key_word,"q=")
        self.url = self.affiche(self.url,'+',self.key_word_in_title,"&qInTitle=")
        self.url = self.affiche(self.url,',',self.sources,"&sources=")
        self.url = self.affiche(self.url,'&language=',self.key_word_in_title,"&language=")

        self.url += '&sortBy=' + self.sortby + '&'
        if self.from_date != 0  :
            self.url += 'from=' + str(self.from_date) + '-00-00&'
        if self.to_date != 0 :
            self.url += 'to=' + str(self.to_date) + '-12-30&'
        self.url += 'apiKey=41ff73330072433da7a7f9b8171e5989'
        print(c.Color("The URL has been sucefully created ! ","g"))
        return self.url


    def get_data(self) : 
        """recupere les donnes et les stockes dans l'attribut result"""
        if len(self.url) == 0 : 
            raise ErrorURL
        self.result = requests.get(self.url).json()
        if len(self.result) == 1 : 
            raise error.FaillureRecupData
        else : 
            print(c.Color("Data had been recovered ! " + str(self.result['totalResults']) + " available articles","g"))
        self.result = self.result['articles']
        for art in self.result : 
            #on nettoi un peu en supprimant toutes les informations qui ne nous serons pas utile
            del art['content']
            del art['urlToImage']
            del art['url']
            del art['publishedAt']

    







ma_recherche = Recherche_article(["Lyon","meilleur",'ville'],[],[],1999,2020,['fr','en'])
ma_recherche.url_everything()
print(ma_recherche.url)
ma_recherche.get_data()


