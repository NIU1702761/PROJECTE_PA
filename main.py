from score import Score
from items import Item, Book, Movie
from user import User
import numpy as np


class Main():

    def __init__(self, fitxer_valoracions):
        
        self._score = Score(fitxer_valoracions)
    
    def recomanacio_simple(self,id_user):
        num_recomanacions = int(input("Numero de recomenacions: "))
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
    

M = Main('prova3.csv')
print(M.recomanacio_simple('U4'))