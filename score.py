#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:22:58 2024

@author: aliciamartilopez
"""

from item import Item, Movie, Book
from user import User
import numpy as np
from typing import List
#from abc import ABCMeta, abstractmethod


class Score:
    
    _ll_usuaris = set 
    _ll_items = set
    _n_usuaris = int 
    _n_items = int
    
    def __init__(self, fitxer_items,fitxer_valoracions,opcio):
        self._ll_usuaris = set()
        self._ll_items = set()
        self._mat = None

        if opcio==1:
            with open(fitxer_valoracions, 'r') as f:
                next(f) 
                for line in f:
                    if len(self._ll_items) < 50000:
                        id_usuari, id_item, _ , _ = line.strip().split(',')
                        self._ll_usuaris.add(id_usuari)
                        self._ll_items.add(id_item)
                    else:
                        break

        elif opcio==2:
            with open(fitxer_items, 'r') as f:
                next(f)
                for line in f:
                    if len(self._ll_items) < 50000:
                        line=line.strip().split(',')
                        id_item = line[0]
                        self._ll_items.add(id_item)
                    else:
                        break
            
            with open('llibres/Users.csv') as f:
                next(f)
                for line in f:
                    line=line.strip().split(',')
                    id_usuari = line[0]
                    self._ll_usuaris.add(id_usuari)


        self._ll_usuaris = list(sorted(self._ll_usuaris))
        self._ll_items = list(sorted(self._ll_items))
        self._n_usuaris, self._n_items = len(self._ll_usuaris), len(self._ll_items)
        self._mat = np.zeros((self._n_usuaris, self._n_items), dtype='float16')


        with open(fitxer_valoracions, 'r') as f:
            next(f) 
            if opcio == 2:
                i = 0
                for line in f:
                    if i < 50000:
                        id_usuari, id_item, score = line.strip().split(',')
                        score = float(score)
                        if id_usuari in self._ll_usuaris and id_item in self._ll_items:
                            self._mat[self._ll_usuaris.index(id_usuari), self._ll_items.index(id_item)] = score
                        i += 1
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
    
    def avg_usu(self, id_usuari) -> float:
        fila=self._mat[self._ll_usuaris.index(id_usuari),:]
        sense_zeros = fila[fila > 0]
        return np.mean(sense_zeros)
    
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
    
    
    
    #def mat_rec_simple(self):
        
    #def __str__(self):
     #   return str(self._mat)

#S = Score('llibres/Ratings.csv',2)


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
