#!/bin/bash

#ON VA OUVRIR TOUTES LES FONCTIONALITES


echo """
from importlib import reload 
from math import *

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
print('		-----		')


print(c.Color('compte.py imported with co','o'))
import compte as co
print('		-----		')

print(c.Color('rech.py imported with r','o'))
import rech as r 
print('		-----		')


mon_article = r.Recherche('https://www.lemonde.fr/planete/article/2020/05/01/coronavirus-dans-le-monde-donald-trump-lie-le-covid-19-a-un-laboratoire-chinois_6038327_3244.html')
cont = list(mon_article.content)


i = 0 
while i < len(cont) : 
	if cont[i] == '<' :
		j=1
		cont[i] = '*'
		while cont[i+j] != '>':
			cont[i+j] = '*'
			j+=1
			

		cont[i+j] = '*'
		i += j 
	else : 
		i +=1 



cont= ''.join(cont).split()

new_cont = []

for i in range(len(cont)) : 
	if (len(cont[i]) > 0) and (len(cont[i]) < 15) and ('|' not in cont[i]) and (':' not in cont[i])  and ('-' not in cont[i])  and ('*' not in cont[i]) and (';' not in cont[i])  and  ('(' not in cont[i]) and (')' not in cont[i]) and ('&' not in cont[i]) and ('=' not in cont[i]) and  ('.' not in cont[i]) and ('[' not in cont[i]) and (']' not in cont[i]) and  ('{' not in cont[i]) and ('}' not in cont[i]) and ('/' not in cont[i]) and ('!' not in cont[i]) and ('?' not in cont[i]): 
		new_cont.append(cont[i])

cont = new_cont.copy()
cont = ' '.join(cont)
print(cont.encode('utf-8').decode('utf-8'))







"""> ~/.lancement_python.py 
export PYTHONSTARTUP=~/.lancement_python.py
python3



