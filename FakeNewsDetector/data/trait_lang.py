import spacy
import color as c

nlp = spacy.load('en_core_web_lg')
print(c.Color("en_core_web_lg has been charged","g"))

from nltk.corpus import stopwords
BADWORDS = list(stopwords.words('english'))
def nettoyer(doc) : 	
	doc = doc.split()
	new = []
	for doc_word in doc : 
		if (doc_word not in BADWORDS + ["'s","n't"]) or (doc_word in ["not","be","have"]): 
			new.append(doc_word)
	return " ".join(new)

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer(language='english')
def degrematiser(doc) : 
	A = [(X,X.pos_) for X in nlp(doc)]
	sentence = []
	for val_A in A : 
		if val_A[1] == 'VERB' : 
			sentence.append(stemmer.stem(str(val_A[0])))
		else : 
			sentence.append(str(val_A[0]))
	return " ".join(sentence)

def neg_or_pos(sentence) : 
	"""determine la positivité ou la négativité de la phrase"""
	A = [(X,X.pos_) for X in nlp(sentence)]
	for val in A : 
		if (str(val[0]) == "n't") or (str(val[0]) == "no") or (str(val[0]) == "not")  :
			return -1
	return 1


def compare_sentence(sentence1,sentence2) : 
	"""donne une valeur de similarité entre les deux phrases"""
	if neg_or_pos(sentence1)*neg_or_pos(sentence2) > 0 : 
		# print(sentence1," -->", nettoyer(degrematiser(sentence1)))
		# print(sentence2," -->", nettoyer(degrematiser(sentence2)))
		sentence1 = nettoyer(degrematiser(sentence1))
		sentence2 = nettoyer(degrematiser(sentence2))

		print(c.Color("Similarité : " + str(nlp(sentence1).similarity(nlp(sentence2))),"g"))

	else : 
		# print(sentence1," -->", nettoyer(degrematiser(sentence1)))
		# print(sentence2," -->", nettoyer(degrematiser(sentence2)))
		print(c.Color("Similarité : 0","r"))



# le GROS de ce module c'est de faire compare_sentence(a,b)

# a = "Watch Dr. Birx react as Trump suggests injecting disinfectant to fight coronavirus"
# b = "Watch Dr. Birx react as Trump suggests injecting disinfectant to fight coronavirus"
# compare_sentence(a,b)