#!/bin/bash

#ON VA OUVRIR TOUTES LES FONCTIONALITES


echo """
from importlib import reload 

import color as c 
print(c.Color('color.py a imported with c','o'))
print('		-----		')

import error as e 
print(c.Color('error.py imported with e','o'))
print('		-----		')


print(c.Color('traducteur.py imported with t','o'))
import traducteur as t 
print('		-----		')


print(c.Color('data.py imported with d','o'))
import data as d 
print('class Recherche_article : ')
print('  def __init__(self,key_words,language) : ')
print('       self.url')
print('       self.key_words')
print('       self.language')
print('       self.result')
print('		-----		')


print(c.Color('compte.py imported with co','o'))
import compte as co
print('		-----		')

print(c.Color('rech.py imported with r','o'))
print('class Recherche : ')
print('  def __init__(self,doc) : ')
print('     doc = titre : ')
print('       self.title')
print('     doc = url ')
print('       self.url')
print('       self.title')
print('       self.publisher')
import rech as r
print('		-----		')


# article_test = {'title': 'Trump says the UK coronavirus plan for herd immunity would have been catastrophic and caused a lot of death', 'description': 'The UKs original plan to deal with the coronavirus by achieving herd immunity within the population, would have been catastrophic and caused a lot of death President Donald Trump has said. The UK reportedly abandoned its original plan for the UK popul…'}

# d.Recherche_article(co.key_words(article_test))



# #1- On recupere les infos sur notre article
# a = r.Recherche('https://edition.cnn.com/2020/04/24/asia/guam-us-air-force-bombers-pull-out-intl-hnk/index.html')
# print(a.title)
# print(a.publisher)

# #2- on trie le titre 
# co.key_words({'title':a.title,'description':''})

# #3- on fait des Recherche d'article similaires
# d.Recherche_article(['US', 'AIR', 'FORCE', 'PULL', 'BOMBERS', 'GUAM'])


a = r.Recherche('https://www.bbc.com/news/health-52413995')
print(a.title)
print( co.stat(a) )

"""> ~/.lancement_python.py 
export PYTHONSTARTUP=~/.lancement_python.py
python3



