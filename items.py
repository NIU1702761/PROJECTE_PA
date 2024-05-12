#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:47:19 2024

@author: aliciamartilopez
"""

import numpy as np
from abc import ABCMeta, abstractmethod

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
        resposta += 'TITOL: '+self._titol+'\n'
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
        resposta += 'AUTOR: '+self._autor+'\n'
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
        resposta += 'GENERES: '+str(self._generes)
        return resposta

"""
nomFitxerValoracions = 'movies/ratings.csv'
nomFitxerTitols = 'movies/movies.csv'


ll_llibres = []
ll_pelis = []



valoracions_llibres ='llibres/Ratings.csv'
titols_llibres = 'llibres/Books.csv'

B = Movie('1',nomFitxerValoracions,nomFitxerTitols)
print(B)
print()
L = Book('074322678X',valoracions_llibres,titols_llibres)
print(L)



"""

