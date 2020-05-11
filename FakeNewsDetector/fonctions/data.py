
import requests
import fonctions.error as e
import fonctions.color as c 

class Recherche_NewAPI : 
    """
    DESCRIPTION 
        this class allows to make research on NewAPI thank to an url or a title

    PARAMETERS
        param1 : list of str
            list of keys words for research
        param2 : list of langage 
            list of lang by default is ["en"]

    ATTRIBUTS 
            self.key_word    
                from - param1 
            self.url   
                made by - self.get_url()
                This url is send to the net for asking data to newAPI
            self.langage     
                from (default) -  ['en']  
            self.sort_by     
                from (default) - 'revelancy'    
            self.result 
                made by - self.get_data()
                This attributs contain a dictionnary with the 100 first article 
            self.nb_art 
                made by - self.get_data()
                This attributs contain the number of articles available 
            self.title 
                made by - self.get_data()
                This attributs is a list containing only the titles

    ERRORS 
        * BadDictio 
            desciption : 
                bad imput type 
            where : 
                __init__()
        * FaillureRecupData
            description : 
                the url send to newAPI give a bad response 
            where : 
                get_data()
    """

    def __init__(self,key_word,langage = ["en"]) : 
        if (type(key_word) != list) or (type(langage) != list):
            """on veut enfait des liste contenant les valeur que l'on veut"""
            raise e.BadDictio
   
        for val in key_word +  langage  : 
            """on verifie que l'on a bien donné des mots"""
            if type(val) != str :
                raise e.BadDictio

        for val in langage : 
            """ le langage ne peut etre que ceux dessous"""
            if val not in  ['ar','de','en','es','fr','he','it','nl','no','pt','ru','se','ud','zh'] : 
                raise e.BadDictio

        self.key_word = key_word
        self.langage = langage
        self.sortby = 'revelancy' 
        self.url = ''

        self.get_url()       # generate URL
        self.get_data()      # get data thank to the url


    @staticmethod
    def affiche(url,sep,list_mot,mot_init) : 
        """
        DESCRIPTION 
            this function is use in the construction of an url it follows the syntax 
            of NewAPI
        """
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
        """
        DESCRIPTION 
            this function  generate an url with the key words 
        """        
        self.url = 'https://newsapi.org/v2/everything?'
        self.url = self.affiche(self.url,'+',self.key_word,"q=")
        self.url = self.affiche(self.url,'&language=',self.langage,"&language=")
        self.url += '&sortBy=' + self.sortby + '&pageSize=100&'
        self.url += 'apiKey=41ff73330072433da7a7f9b8171e5989'
        print(c.Color("The URL has been sucefully created ! ","g"))


    def get_data(self) : 
        """
        DESCRIPTION 
            this function gets data from internet using the URL created by get_url 
            It allows to have : 
                    self.nb_art
                    self.result : dictionnary withe all articles and their informations 
                    self.title  : a list withe only the title
        """ 
        self.result = requests.get(self.url).json()
        if len(self.result) == 1 : 
            # the response of NewAPI is empty ... 
            raise e.FaillureRecupData

        self.nb_art = self.result['totalResults']
        self.result = self.result['articles']
        self.title = []
        for art in self.result : 
            # we recup only the titles and not all the informations for each article
            self.title.append(art['title'])
        print(c.Color("Data had been recovered ! " + str(self.nb_art) + " available articles","g"))

