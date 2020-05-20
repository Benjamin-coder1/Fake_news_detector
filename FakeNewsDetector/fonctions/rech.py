import urllib.request 
import error 
import color as c
import trait_lang as tl
import operator 

class Recherche_On_Article : 
	"""
	DESCRIPTION 
	    this class allows to make research on a specifical article on the net

	PARAMETERS
	    param1 : str
	        This is the article, either the url (best) or just the title

	ATTRIBUTS 
		IF param1 is an url : 
        self.url    
            from - param1 
        self.content   
            created in - __init__()
            This contain all the code html of the page 
        self.publisher     
            made by -  get_infos()         from (default) - ''
        self.text   
            created in - get_info()
            This contain the content of the article  


		IF param1 is a title : 
        self.title    
            from - param1 
        self.
                     
	ERRORS 
	    * BadUrl 
	        desciption : 
	            The url doesn't give us acces to what we need it can be because of right acces or 
	            because the code of the page is a little bit different of what we expect or again the information 
	            isn't in the code (unlikely) 
	        where : 
	            get_info()
	    * get_combi_key_words
	        description : 
	            we gave just a title and not an url so we can't use the methods get_stat() and get_combi_key_words()
	        where : 
	            get_combi_key_words()
	            get_stat()

	"""

	def __init__(self,doc) : 
		if "https://" in doc :
			# GREAT !  we have an url we are going to recover a lot of data 
			self.url = doc
			#we make a request on the net to recover the code of the page of the url it is html code
			try : 
				self.content = urllib.request.urlopen(self.url).read().decode('utf-8')   
			except : 
				pass 
			if not hasattr(self,"content") : 
				print("helllllllllllllo")
				raise error.BadUrl
			print(c.Color("Content has been charged it is an URL","g"))
			self.publisher = ""
			#we recover now data in self.content ! 
			self.get_info() 

		else : 
			# On recoit un titre en entrée
			self.title = doc 
			print(c.Color("Content has been charged it is just a title","g"))

	@staticmethod
	def get_from_to(contenue,mot1, mot2) : 
		"""
		DESCRIPTION 
		    this function is used to recover good data from self.content 
		    it recover all the data in contenue situated between mot1 and mot2
		
		PARAMETERS
		    param1 : str
		        This is the str in which we will make research 
		    param2 : str
		        word of start
		    param3 : str
		        word of end 

		OUTPUT : 
			out1 : str
				All what is between param2 and param3 in param1

		"""		
		j = 0
		deb = 0
		fin = 0
		while (fin == 0) and (j < (len(contenue)+len(mot1) + len(mot2))) : 
			if contenue[j:(j+len(mot1))] == mot1 : 
				deb = j
			if (contenue[j:(j+len(mot2))] == mot2) and (deb != 0): 
				fin = j
			j +=1
		if deb == fin : 
			# we have traveled all the sentence without finding mot1
			return None
		return contenue[(deb+len(mot1)):fin]

	def get_info(self) :
		"""
		DESCRIPTION 
		    this function is used to get all the informations we need in the code of the page
		    which is in self.content 
		    it must be used only if we have an url and not just a title !!
		"""

		# ------- we start recovering the title (necessary ) -------
		self.title = self.get_from_to(self.content, "<title", "</title>")
		if self.title is None : 
			# we don't find the title we can't continue
			raise error.BadUrl
		print(c.Color("Title recup","t"))


		# ------- we try to recover the name of the publisher -------
		# we can need it because in manay case the name of the publisher is also in the title 
		# and it create a lot of problems in the search of key words ... 
		# We recover the title in the url
		
		if "https://www." in self.url : 
			i =  len("https://www.")
			while self.url[i:(i+3)] != ".co" : 
				self.publisher += self.url[i]
				i += 1
			print(c.Color("Publisher recup","t"))
		else :  
			i =  len("https://")
			while self.url[i:(i+3)] != ".co" : 
				self.publisher += self.url[i]
				i += 1
			print(c.Color("Publisher recup","t"))

		# ------- we try to recover only the text of the article -------
		i=0 
		self.text = []
		while i < len(self.content) : 
			# in html the content of a graph is usually situated between <p> and </p> so we try to recover 
			# all the sence we can 
			if (self.content[i] == "<") and (self.content[i+1] == "p") and (self.content[i+2] == ">") : 
				i += 3
				while (self.content[i] != "<") or (self.content[i+1] != "/") or (self.content[i+2] != "p") or (self.content[i+3] != ">") :
					self.text.append(self.content[i])
					i +=1
				i += 4 
				self.text.append(" ")
			else : 
				i += 1

		# we supress all the code of the shapping < ..... code ...... >
		i = 0
		while i < len(self.text) : 
			if self.text[i] == "<" : 
				while self.text[i] != ">" : 
					self.text[i] = ""
					i += 1
				self.text[i] = ""
			else : 
				i += 1
		self.text = "".join(self.text).lower()



		if len(self.text) <  1000 : 
			# sometime the text isn't between <p> and </p> so we are going to analyse all the words of the code
			# it is not extraordary but it is better than nothing
			self.text = self.content.split()
			new = []
			for mot in self.text : 
				if len(mot) < 15 : 
					new.append(mot)
			self.text = " ".join(new)
			print(c.Color("all code recup","t"))
		else : 
			print(c.Color("good text recup","t"))

	
	def get_stat(self) : 
	    """
	    DESCRIPTION 
	        this function is used to get the statistic of each words in the title in the text of the article  
	        WE NEED THE URL !  		    
	    """	   

	    if not hasattr(self, "text") : 
	    	# we check if we have the content of the article for using the get_stat() method
	    	raise error.FaillureRecupData


	    # we create a dictionnary which will associate to each word in the title it's occurence in the article
	    key_words_sentence = {}

	    # we use the module trait_lang in order to suppress the conjugaison / plural /  's ... 
	    # this was not in the first part in the code but now that we have these fonctions it is logical to use them 
	    # they allows to have so much better result
	    clean_text = tl.degrematiser(self.text).lower()
	    # we suppress in the title all the "stop words" useless for understanding the sens of the sentence 
	    TITLE = tl.nettoyer(self.title).split()
	    # Now we complete the dictionnary 
	    for TITLE_word in TITLE : 
	    	if TITLE_word not in [" ","-",":","!","?","'"] : 
	    		key_words_sentence[TITLE_word] = clean_text.count(tl.degrematiser(TITLE_word.lower()))
	    return key_words_sentence


	def get_key_words_nlp(self) : 
	    """
		DESCRIPTION 
		    this function is used to get the key words using the nlp thank to an analyse of the title it is only 
		    for the second part 
		    WE NEED JUST THE TITLE ! 

		OUTPUT : 
			out1 : list of str
				this is the list of the main entities of the sentence find by spacy 
		    
		"""
	    #------- we supress the ponctuation and the publisher (if we know him) ------ 
	    # we start with ponctuation 
	    self.title = list(self.title)
	    new = []
	    for cara in self.title : 
	    	# if cara is in the following list we dont keep it 
	    	if cara not in ["-",":","!","?","'","|"] : 
	    		new.append(cara)
	    self.title = "".join(new)

	    #we continue with the publisher
	    if hasattr(self,"publisher") and (len(self.publisher) != 0) : 
	        #we check if publisher exister and is not empty
	        self.title = self.title.split()
	        for title_words in self.publisher.split(): 
	        	#we suppress it from the title
	        	while title_words in self.title : 
	        		self.title.remove(title_words)
	        self.title = " ".join(self.title)

	    #------- we use spacy to find the key actors / organisations / groups ... ------ 

	    # The following code line allows to recover a dictionnary with the entities 
	    # this is based on the nlp, spacy is able to analyse the sentence to do that ! 
	    A = [(X.text,X.label_) for X in tl.nlp(tl.nettoyer(self.title)).ents]
	    actors = []
	    for A_word in A : 
	    	# we keep only the groups/organisation/people date is not necessary 
	    	if A_word[1] not in  ['CARDINAL','DATE'] : 
	    		actors += str(A_word[0]).split()
	    return actors


	def get_combi_key_words(self) : 
	    """
		DESCRIPTION 
		    the role of this function is to combine the 2 previous methods in order to have the more results possible
		    It create a list of list, each list is a list of key words that will be used in order to make research on NewAPI
		    We start by taking the list of entities created by the previous method, then we create new list adding words of the title 
		    depending of their occurence in the title (the more they have, the more they are added quickly) 
		    WE NEED THE URL ! 

		OUTPUT : 
			out1 : list of str
				each list of the list of the output will be used to make a research ! 
		    
		"""
	    if not hasattr(self, "text") : 
	    	# we check if we have the content of the article for using the get_stat() method
	    	raise error.FaillureRecupData

		# we recover the actors 
	    actors = self.get_key_words_nlp()

	    # we recover the statistics of each word of the title 
	    stat = self.get_stat()

	    combi_key_words = []
	    combi_key_words.append(actors)
	    
	    while len(stat) != 0 :  
	    	# we create a new list made by the last list of combi_key_words and the title's word with the best occurence 
	    	mot_max = max(stat.items(), key=operator.itemgetter(1))[0]
	    	if mot_max not in combi_key_words[-1] :
	    		# we check this is not a word which is ever in actor
	    		print(combi_key_words[-1] + [mot_max])
	    		combi_key_words.append(combi_key_words[-1] + [mot_max]) 
	    	del stat[mot_max]

	    return combi_key_words

	    










