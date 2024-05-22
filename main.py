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
        fitxer_pelis = 'movies/movies.csv'
        fitxer_llibres = 'llibres/Books.csv'
        
        
        o = int(input('\nConjunt de dades:\n    1 - pelicules\n    2 - llibres\n --> '))
        while (o != 1) and (o != 2):
            print('Opció invalida.')
            o = int(input('\nConjunt de dades:\n    1 - pelicules\n    2 - llibres\n --> '))
        print('Carregant conjunt de dades...')
        if o == 1:
            self._score = Score(fitxer_pelis,fitxer_valoracions_pelis,o)
        else:
            self._score = Score(fitxer_llibres,fitxer_valoracions_llibres,o)
        #metode = 1
        print('Fet!')
        self.crida_metode(o)

    def crida_metode(self,o):
        fitxer_valoracions_pelis = 'movies/ratings.csv'
        fitxer_valoracions_llibres = 'llibres/Ratings.csv'

        metode = int(input('\nMètode de recomanació:\n    1 - recomanacio_simple\n    2 - recomanació_colaborativa\n --> '))
        while (metode != 1) and (metode != 2):
            print('Opció invàlida.')
            metode = int(input('\nMètode de recomanació:\n    1 - recomanacio_simple\n    2 - recomanació_colaborativa\n --> '))
        id_user = input("\nIdentificador d'usuari: ")
        #id_user = '276725'
        #276746
        while id_user != '':
            R = Recomanacio(self._score, id_user)
            if metode == 1:
                items = R.recomanacio_simple()
            else:
                k=int(input("Nombre d'usuaris a considerar (k):"))
                items = R.recomanacio_colaborativa(k)
            
            for item in items:
                if o == 2:
                    H = Book(item,fitxer_valoracions_llibres,'llibres/Books.csv')
                    if H:
                        print('\n'+str(H))
                    else:
                        print('Llibre no carregat')
                else:
                    H = Movie(item,fitxer_valoracions_pelis, 'movies/movies.csv')
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