
import requests
import error 
import color as c 


class Recherche_article : 

    def __init__(self,key_word,langage = ["en"]) : 
        if (type(key_word) != list) or (type(langage) != list):
            """on veut enfait des liste contenant les valeur que l'on veut"""
            raise error.BadDictio
   
        for val in key_word +  langage  : 
            """on verifie que l'on a bien donné des mots"""
            if type(val) != str :
                raise error.BadDictio

        for val in langage : 
            """ le langage ne peut etre que ceux dessous"""
            if val not in  ['ar','de','en','es','fr','he','it','nl','no','pt','ru','se','ud','zh'] : 
                raise error.BadDictio

        self.key_word = key_word
        self.langage = langage
        self.sortby = 'revelancy' 
        self.url = ''

        self.get_url()
        self.get_data()


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

    def get_url(self) : 
        """on va générer une URL pour everything grace au attribut de recherche"""
        self.url = 'https://newsapi.org/v2/top-headlines?'
        self.url = self.affiche(self.url,'+',self.key_word,"q=")
        self.url = self.affiche(self.url,'&language=',self.langage,"&language=")
        self.url += '&sortBy=' + self.sortby + '&'
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
            del art['urlToImage']
            del art['url']
            del art['publishedAt']
            del art['source']
            del art['author']


    


