#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:24:12 2024

@author: aliciamartilopez
"""

import numpy as np
from abc import ABCMeta, abstractmethod

class Item(metaclass=ABCMeta):

    _titol: str
    #_valoracions: dict = {}
    _ID: str
    _extra: str #Tercera columna, generes per un i autor per altre


    def __init__(self, ID=0, nomFitxerValoracions="", nomFitxerTitols=""):
        self._titol = ""
        self._ID = ID
        with open(nomFitxerTitols, 'r', encoding='utf-8') as f:
            for line in f:
                elements = line.strip().split(',')
                if elements[0] == str(self._ID):  
                    if elements[1].startswith('"'):
                        fi=False
                        while not fi:
                            elements[1]+=","+elements[2]
                            if '"' in elements[2]:
                                fi=True
                            j=3
                            while j<len(elements):
                                elements[j-1]=elements[j]
                                j+=1
                            elements.pop()
                        
                    self._titol=elements[1]
                    self._extra=elements[2]
                    break


    def __str__(self):
        
        if self._titol:
            resposta = ''
            resposta += 'TITOL: '+self._titol+'\n'
            return resposta
        else: 
            return None
        


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
        if self._titol:
            resposta = super().__str__()
            resposta += 'AUTOR: '+self._autor+'\n'
            return resposta
        else:
            return None

class Movie(Item):
    _generes: list = []

    def __init__(self, ID = 0, nomFitxerValoracions = "", nomFitxerTitols = "", generes = []):
        super().__init__(ID, nomFitxerValoracions, nomFitxerTitols)
        self._generes = self._extra[:].split('|')

    def __str__(self):
        if self._titol:
            resposta = super().__str__()
            resposta += 'GENERES: '+str(self._generes)
            return resposta
        else:
            return None

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

