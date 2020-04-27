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

co.note('https://edition.cnn.com/2020/04/27/asia/kim-jong-un-health-letter-south-african-president-intl/index.html')



"""> ~/.lancement_python.py 
export PYTHONSTARTUP=~/.lancement_python.py
python3



