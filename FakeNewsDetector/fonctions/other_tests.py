import urllib.request 
import rech 
import error



def get_list_fake_sources() : 
	"""
	DESCRIPTION 
	    this function is used to recover a list of web sites gessed as carriers 
	    of fake news

	PARAMETERS
	    None

	OUTPUT : 
		out1 : list
			The list of the web sites
	"""		

	# we recover the data from wikipedia 
	url_data_base = "https://en.wikipedia.org/wiki/List_of_fake_news_websites"
	content = urllib.request.urlopen(url_data_base).read().decode('utf-8')  
	
	def clean(deb,fin) : 
		# operation nedeed to clean the data in useless informations 
		k = 0
		while k < len(lst[-1]):
			if lst[-1][k] == deb : 
				while lst[-1][k] != fin :
					lst[-1][k] = ""
					k += 1
				lst[-1][k] = ""
			else : 
				k += 1
	
	# we are goig to recover the titles and to stock them in lst
	i = 0
	lst = []
	while i < len(content) : 
		# we range the code of the page the info is between : 
		#     <tr>\n<td>  ----title-----  </td>
		if content[i:i+9] == '<tr>\n<td>' : 
			# we have founded a title 
			lst.append([])
			i += 9
			while content[i:i+5] != "</td>" : 
				lst[-1].append(content[i])
				i += 1
			lst[-1].remove('\n')
			# We remove all what is not the title (links then other informations)
			clean('<','>')
			clean('(',')')
			
			lst[-1] = "".join(lst[-1])
		else : 
			# this is not the begining of a title 
			i += 1

	return lst


def other_test_1_test_on_publisher(article) : 
	"""
	DESCRIPTION 
	    this function is used to give a note to an article
	    If the publisher is in get_list_fake_sources() we give the note of 0 else the note is 1

	PARAMETERS
	    param1 : article
	        This must be our article 
	 
	OUTPUT : 
		out1 : int
			0 or 1

	"""		
	if not isinstance(article,rech.Recherche_On_Article) :
		# here we have a bad input 
		raise error.FaillureRecupData

	if hasattr(article,"publisher") : 
		# we have a publisher so we look if publisher is in the list of kake new publishers
		for fake in get_list_fake_sources() : 
			if "".join(fake.lower().split()) in article.publisher.lower() : 
				return 0

	return 1


