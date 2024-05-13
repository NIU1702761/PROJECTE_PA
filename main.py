#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:23:24 2024

@author: aliciamartilopez
"""

from score import Score
from item import Item, Book, Movie
from user import User
import numpy as np


class Main2():

    def __init__(self):
        fitxer_valoracions_pelis = 'movies/ratings.csv'
        fitxer_valoracions_llibres = 'llibres/Ratings.csv'
        fitxer_valoracions_prova = 'prova3.csv'
        #o = 2
        o = int(input('\nAmb quin conjunt de dades vols treballar?\n1 - pelicules\n2 - llibres\n3 - prova\n'))
        if o == 1:
            self._score = Score(fitxer_valoracions_pelis,o)
        elif o == 2:
            self._score = Score(fitxer_valoracions_llibres,o)
        else:
            self._score = Score(fitxer_valoracions_prova,o)
        #metode = 1
        metode = int(input('\nQuin mètode de recomanació vosl fer servir?\n1 - recomanacio_simple\n2 - recomanació_colaborativa\n'))
        if metode == 1:
            id_user = input("Identificado d'usuari: ")
            #id_user = '276725'
            #276746
            while id_user != '':
                items = self.recomanacio_simple(id_user)
                for item in items:
                    if o == 2:
                        H = Book(item,fitxer_valoracions_llibres,'llibres/Books.csv')
                        #print('\n'+str(Book(item,fitxer_valoracions_llibres,'llibres/Books.csv')))
                        if H:
                            print('\n'+str(H))
                        else:
                            print('Llibre no carregat')
                    else:
                        H = Movie(item,fitxer_valoracions_pelis,'movies/movies.csv')
                        #print('\n'+str(Movie(item,fitxer_valoracions_pelis,'movies/movies.csv')))
                        if H:
                            print('\n'+str(H))
                        else:
                            print('Película no carregada')
                id_user = input("Identificado d'usuari: ")
    
    def recomanacio_simple(self,id_user):
        #num_recomanacions = 1
        num_recomanacions = int(input("Numero de recomenacions: "))
        #min_vots = 1
        min_vots = int(input('Minim vots: '))
        items_a_considerar = self._score.min_vots(min_vots)
        
        puntuacions = []
        avg_global = self._score.avg_global(items_a_considerar)
        
        for id_item in items_a_considerar:
            num_vots = self._score.num_vots(id_item)
            avg_item = self._score.avg_item(id_item)
            puntuacio = ((num_vots/(num_vots+min_vots))*avg_item)+((min_vots/(num_vots+min_vots))*avg_global)
            puntuacions.append(puntuacio)
        
        items = []
        copia_puntuacions = puntuacions.copy()
        while len(items) < num_recomanacions:
            maxim = max(copia_puntuacions)
            id_item = items_a_considerar[puntuacions.index(maxim)]
            if self._score.no_vista(id_user, id_item):
                items.append(id_item)
            copia_puntuacions.remove(maxim)
            
        return items
    
    #def recomanacio_colaborativa(self, id_user):
            
        
    

M = Main2()

#valoracions_llibres ='llibres/Ratings.csv'
#titols_llibres = 'llibres/Books.csv'
#print(M.recomanacio_simple('U4'))
#nomFitxerValoracions = 'movies/ratings.csv'
#nomFitxerTitols = 'movies/movies.csv'