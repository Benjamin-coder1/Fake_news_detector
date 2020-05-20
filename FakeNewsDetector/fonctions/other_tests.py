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


def test_on_publisher(article) : 
	if not isinstance(article,rech.Recherche_On_Article) :
		raise error.FaillureRecupData

	if hasattr(article,"publisher") : 
		# On dispose du publieur 
		if article.publisher in get_list_fake_sources() : 
			return 0

	elif hasattr(article,"content") : 
		for web_site in get_list_fake_sources() : 
			if web_site in article.content : 
				return 0
	return 1

