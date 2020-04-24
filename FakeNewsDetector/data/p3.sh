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
print('		-----		')


print(c.Color('tweet.py imported with t','o'))
import tweet as t 
print('		-----		')

print(c.Color('compte.py imported with co','o'))
import compte as co
print('		-----		')

co.stat('donald est mort')





"""> ~/.lancement_python.py 
export PYTHONSTARTUP=~/.lancement_python.py
python3



