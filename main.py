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
from recomanacions import Recomanacio

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
                R = Recomanacio(self._score, id_user)
                items = R.recomanacio_simple()
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
    
    #def recomanacio_colaborativa(self, id_user):
            
        
    

M = Main2()

#valoracions_llibres ='llibres/Ratings.csv'
#titols_llibres = 'llibres/Books.csv'
#print(M.recomanacio_simple('U4'))
#nomFitxerValoracions = 'movies/ratings.csv'
#nomFitxerTitols = 'movies/movies.csv'