
import requests
import error 

#self. {'key_word,'key_word_in_title':,'sources':,'from_date':,'to_date':,'langage':,'sortby':}

class Recherche_article : 

    def __init__(self,key_word,key_word_in_title,sources,from_date,to_date,langage) : 
        if (type(key_word) != list) and (type(key_word_in_title) != list) and (type(sources) != list) and (type(langage) != list):
            """on veut enfait des liste contenant les valeur que l'on veut"""
            raise error.BadDictio
   
        if (type(from_date) != int ) and (type(to_date) != int) :
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

    
    def url_everything(self) : 
        """on va générer une URL pour everything grace au attribut de recherche"""
        self.url = 'https://newsapi.org/v2/everything?'
        for val in self.key_word : 
            self.url += 'q=' + val +'&'
        for val in self.key_word_in_title : 
            self.url += 'qInTitle=' + val + '&'
        for val in self.sources : 
            self.url += 'sources=' + val + '&'
        for val in self.langage : 
            self.url += 'language=' + val + '&'

        self.url += 'sortBy=' + self.sortby
        if self.from_date != 0 and self.to_date == 0 :
            self.url += 'from=' + self.from_date +'&to-' + self.to_date 
        if self.from_date != 0 and self.to_date == 0 :
            self.url += 'from=' + self.from_date 
        if self.from_date == 0 and self.to_date != 0 :
            self.url += 'to=' + self.to_date 
        self.url += '&apiKey=41ff73330072433da7a7f9b8171e5989'
        print("The URL has been sucefully created ! ")
        return self.url

    def url_top_headlines(self) : 
        """on va générer une URL pour everything grace au attribut de recherche"""
        self.url = 'https://newsapi.org/v2/top-headlines?'
        for val in self.key_word : 
            self.url += 'q=' + val +'&'
        for val in self.key_word_in_title : 
            self.url += 'qInTitle=' + val + '&'
        for val in self.sources : 
            self.url += 'sources=' + val + '&'
        for val in self.langage : 
            self.url += 'language=' + val + '&'

        self.url += 'sortBy=' + self.sortby
        if self.from_date != 0 and self.to_date == 0 :
            self.url += 'from=' + self.from_date +'&to-' + self.to_date 
        if self.from_date != 0 and self.to_date == 0 :
            self.url += 'from=' + self.from_date 
        if self.from_date == 0 and self.to_date != 0 :
            self.url += 'to=' + self.to_date 
        self.url += '&apiKey=41ff73330072433da7a7f9b8171e5989'
        print("The URL has been sucefully created ! ")
        return self.url


    def get_data(self) : 
        """recupere les donnes et les stockes dans l'attribut result"""
        if len(self.url) == 0 : 
            raise ErrorURL
        else : 
            self.result = requests.get(self.url).json()
            if self.result['status'] != 'ok' : 
                raise error.FaillureRecupData
            else : 
                print("Data had been recovered ! {} available articles".format(self.result['totalResults']))





ma_recherche = Recherche_article(["covid","hello"],[],[],1200,1300,['es','fr'])




