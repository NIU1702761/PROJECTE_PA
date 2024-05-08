#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from abc import ABCMeta, abstractmethod


#a = len(NOM_FITXER_USUARIS.readlines())
#b = len(NOM_FITXER_ITEMS.readlines())

#Valoracions = np.empty(a,b)
# a --> usuaris
# b --> IDs de items

#Items = np.empty(b,b)

#NOM_FITXER_ITEMS = 'llibres/Books.csv'
#NOM_FITXER_USUARIS = 'llibres/Users.csv'
#NOM_FITXER_VALORACIONS = 'llibres/Ratings.csv'
#with open(NOM_FITXER_VALORACIONS, 'r') as file1, open(NOM_FITXER_ITEMS, 'r') as file2:
   #for line in zip(file1, file2): 
       
       #line = line.split(',')
        

#ftixer_pelis = 'pelis.csv'
#fitxer_llibres = 'llibres.csv'

#nomFitxerValoracions = 'movies/ratings.csv'
#nomFitxerTitols = 'movies/movies.csv'

class Item(metaclass=ABCMeta):

    _titol: str
    _valoracions: dict = {}
    _ID: str


    def __init__(self, ID = 0, nomFitxerValoracions = "", nomFitxerTitols = ""):

        self._ID = ID
        self._valoracions = {}
        with open(nomFitxerValoracions, 'r') as f:
            for line in f:
                line = line.split(',')
                if line[1] == self._ID:
                    self._valoracions[line[0]] = line[2]
        with open(nomFitxerTitols, 'r') as f:
            for line in f:
                line = line.split(',')
                if line[0] == self._ID:
                    self._titol = line[1]
    
    def __str__(self):
        resposta = ''
        resposta += self._titol+'\n'
        return resposta


class Book(Item):

    _autor: str


    def __init__(self, ID = 0, nomFitxerValoracions = "", nomFitxerTitols = "", autor = ""):

        super().__init__(ID, nomFitxerValoracions, nomFitxerTitols)
        with open(nomFitxerTitols, 'r') as f:
            for line in f:
                line = line.split(',')
                if line[0] == self._ID:
                    self._autor = line[2]
    
    def __str__(self):
        resposta = super().__str__()
        resposta += self._autor+'\n'
        return resposta

class Movie(Item):
    _generes: list = []

    def __init__(self, ID = 0, nomFitxerValoracions = "", nomFitxerTitols = "", generes = []):
        super().__init__(ID, nomFitxerValoracions, nomFitxerTitols)
        with open(nomFitxerTitols, 'r') as f:
            for line in f:
                line = line.split(',')
                if line[0] == self._ID:
                    self._generes = line[2][:-1].split('|')
    def __str__(self):
        resposta = super().__str__()
        resposta += str(self._generes)
        return resposta

nomFitxerValoracions = 'movies/ratings.csv'
nomFitxerTitols = 'movies/movies.csv'


ll_llibres = []
ll_pelis = []



valoracions_llibres ='llibres/Ratings.csv'
titols_llibres = 'llibres/Books.csv'
B = Movie('1',nomFitxerValoracions,nomFitxerTitols)
print(B)
L = Book('074322678X',valoracions_llibres,titols_llibres)
print(L)


#with open(titols_llibres) as f:
    




