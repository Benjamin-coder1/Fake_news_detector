import spacy
import fonctions.color as c


# we are going to use spacy to make analyse of sentences using NLP and machine learning and 
# to compare sentences what we need 

# We try by chatrging the following module containing 1 million of words (loading can be a little long)
nlp = spacy.load('en_core_web_lg')
print(c.Color("en_core_web_lg has been charged","g"))



# ------- Cleaning sentence suppressing stopWords -------
# we use a module find on the net 
from nltk.corpus import stopwords
BADWORDS = list(stopwords.words('english'))

def nettoyer(doc) : 	
	"""
	DESCRIPTION 
	    this function is use in order to clean the sentences of the stop words

	PARAMETERS
	    param1 : str
	        This is the sentence to clean 

	OUTPUT  
		out1 : str
			clean sentence
	"""
	doc = doc.split()
	new = []
	for doc_word in doc : 
		# we keep only the words not in BADWORDS however we also keep the words negation, we will need them later 
		if (doc_word not in BADWORDS + ["'s","n't"]) or (doc_word in ["not","be","have"]): 
			new.append(doc_word)
	return " ".join(new)


# ------- Cleaning sentence suppressing grammary, plural, conjugaison, constructions ... -------
# All of that reduce the result of the comparison on sentence, we just need the root of the words
# we use a module of NLP find on the net 
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer(language='english')

def degrematiser(doc) : 
	"""
	DESCRIPTION 
	    this function is use in order to keep only the root of words

	PARAMETERS
	    param1 : str
	        This is the sentence to clean 

	OUTPUT  
		out1 : str
			clean sentence
	"""
	A = [(X,X.pos_) for X in nlp(doc)]
	sentence = []
	for val_A in A : 
		if val_A[1] != 'PROPN' : 
			# if the word is a name we don't change it ! 
			sentence.append(stemmer.stem(str(val_A[0])))
		else : 
			sentence.append(str(val_A[0]))
	return " ".join(sentence)

# ------- Function on comparison of sentences -------

def neg_or_pos(sentence) : 
	"""
	DESCRIPTION 
	    this function analasy the negation of the sentence, if a word of negation is find we considere the 
	    sentence is negative 

	PARAMETERS
	    param1 : str
	        This is the sentence to clean 

	OUTPUT  
		out1 : int
			1 if the sentence is positive / -1 is it is negative
	"""	
	A = [(X,X.pos_) for X in nlp(sentence)]
	# this code line decompose the sentence and analyse the type of each word (NOUN/VERB/PART ... )
	for val in A : 
		if (str(val[0]) == "n't") or (str(val[0]) == "no") or (str(val[0]) == "not")  :
			return -1
	return 1


def compare_sentence(sentence1,sentence2) : 
	"""
	DESCRIPTION 
	    this function compare 2 sentences using the similarity function of spacy 

	PARAMETERS
	    param1 : str
	        first sentence to compare
	    param2 : str
	        second sentence to compare

	OUTPUT  
		out1 : int
			out1 is in [0,1]     0 -> any similarities    1-> the same sentences  
	"""		

	# similarity is no able to distinguish effectively the negation so we do it that to neg_or_pos() 
	if neg_or_pos(sentence1)*neg_or_pos(sentence2) > 0 : 
		# both positive or negative
		# we clean the sentences thank to the last functions
		sentence1 = nettoyer(degrematiser(sentence1))
		sentence2 = nettoyer(degrematiser(sentence2))
		# we compare them with the amazing following function of spacy !
		simi = nlp(sentence1).similarity(nlp(sentence2))
		print(c.Color("Similarité : " + str(simi),"g"))
		return simi
	else : 
		# one positive one negative
		print(c.Color("Similarité : 0","r"))
		return 0
