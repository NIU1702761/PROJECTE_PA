#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:32:01 2024

@author: aliciamartilopez
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:36:35 2024

@author: aliciamartilopez
"""
from items import Item, Movie, Book
from user import User
import numpy as np
from typing import List
#from abc import ABCMeta, abstractmethod


class Score:
    
    _ll_usuaris = set 
    _ll_items = set
    _n_usuaris = int 
    _n_items = int
    
    def __init__(self, fitxer_valoracions,opcio):
        self._ll_usuaris = set()
        self._ll_items = set()
        self._mat = None

        with open(fitxer_valoracions, 'r') as f:
            next(f) 
            if opcio == 2:
                for line in f:
                    if len(self._ll_items) < 100000:
                        id_usuari, id_item, _ = line.strip().split(',')
                        self._ll_usuaris.add(id_usuari)
                        self._ll_items.add(id_item)
                    else:
                        break
            else: 
                for line in f:
                    id_usuari, id_item, _ , _ = line.strip().split(',')
                    self._ll_usuaris.add(id_usuari)
                    self._ll_items.add(id_item)

        self._ll_usuaris = list(sorted(self._ll_usuaris))
        self._ll_items = list(sorted(self._ll_items))
        self._n_usuaris, self._n_items = len(self._ll_usuaris), len(self._ll_items)
        self._mat = np.zeros((self._n_usuaris, self._n_items))

        with open(fitxer_valoracions, 'r') as f:
            next(f) 
            if opcio == 2:
                for line in f:
                    if len(self._ll_items) < 100000:
                        id_usuari, id_item, score = line.strip().split(',')
                        score = float(score)
                        self._mat[self._ll_usuaris.index(id_usuari), self._ll_items.index(id_item)] = score
                    else:
                        break
            else:
                for line in f:
                    id_usuari, id_item, score, _ = line.strip().split(',')
                    score = float(score)
                    self._mat[self._ll_usuaris.index(id_usuari), self._ll_items.index(id_item)] = score 
    
    def min_vots(self,min_vots):
        ll = []
        for index, id_item in enumerate(self._ll_items):
            if np.count_nonzero(self._mat[:,index]) >= min_vots:
                ll.append(id_item)
        return ll
    
    
    def avg_item(self, id_item) -> float:
        """
        avg_item: valoració mitja que li han donat els usuaris a l’ítem (considerant
        només els vots rebuts, descartem valoracions amb un 0).
        """
        columna = self._mat[:,self._ll_items.index(id_item)]
        sense_zeros = columna[columna > 0]
        return np.mean(sense_zeros)
    
    def num_vots(self, id_item):
        """
        num_vots: nº d’usuaris que han puntuat aquest ítem
        """
        columna = self._mat[:, self._ll_items.index(id_item)]
        return np.count_nonzero(columna)
    
    def avg_global(self, ll_id_items):
        """
        avg_global: valoració mitja de tots els ítems considerats
        """
        suma = 0
        for id_item in ll_id_items:
            suma += self.avg_item(id_item)
        return suma/len(ll_id_items)

    def no_vista(self, id_usuari, id_item):
        if self._mat[self._ll_usuaris.index(id_usuari), self._ll_items.index(str(id_item))] == 0:
            return True
        else:
            return False
        
    #def __str__(self):
     #   return str(self._mat)

S = Score('llibres/Ratings.csv',2)


"""
U= Score('movies/ratings.csv')
#U = Score('prova2.csv')

print('mtjana de la peli 1:')
print(U.avg_item('2'))
print('quanta gent ha votat la peli 1: ')
print(U.num_vots('1'))
#print('pelis que tenen minim 3 votacions: ')
#print(U.min_vots(3))
print('valoració mitja de tots els ítems considerats: ')
print(U.avg_global(U.min_vots(3)))
"""
