from score import Score
from item import Item, Book, Movie
from user import User
import numpy as np
from math import sqrt


class Recomanacio():

    def __init__(self, score, id_user):
        self._id_user = id_user
        self._score = score
            
    def recomanacio_simple(self):
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
            if self._score.no_vista(self._id_user, id_item):
                items.append(id_item)
            copia_puntuacions.remove(maxim)
            
        return items
    
    def similitud(self,usuari_client,usuari_secundari):
        numerador=0
        denominador1=0
        denominador2=0
        index_usu_client=self._score._ll_usuaris.index(usuari_client) #Trobar índex d'usuari a la matriu
        index_usu_sec=self._score._ll_usuaris.index(usuari_secundari)
        num_rows, _ = self._score._mat.shape
        for j in range(num_rows):
            v_usuari_client=self._score._mat[index_usu_client][j]
            v_usuari_secundari=self._score._mat[index_usu_sec][j]
            if v_usuari_client!=0 and v_usuari_secundari!=0:
                numerador+=v_usuari_client*v_usuari_secundari
                denominador1+=(v_usuari_secundari)**2
                denominador2+=(v_usuari_client)**2
        
        if numerador!=0 and denominador1!=0 and denominador2!=0:
            return numerador/(sqrt(denominador1)*sqrt(denominador2))
        else:
            return 0


    def recomanacio_colaborativa(self,k):
        similituds=[]
        for usuari in self._score._ll_usuaris:
            s=self.similitud(self._id_user,usuari)
            similituds.append((usuari,s))
        
        similituds.sort(key=lambda x: x[1], reverse=True)
        k_similituds = similituds[:k+2][1:]
        usuaris_similars = [x[0] for x in k_similituds]
        
        puntuacions=[]
        mitjana_usu=self._score.avg_usu(self._id_user)
        for item in self._score._ll_items:
            numerador=0
            denominador=0
            if self._score.no_vista(self._id_user, item):
                for usuari in usuaris_similars:
                    i=usuaris_similars.index(usuari)
                    mitjana=self._score.avg_usu(usuari)
                    numerador+=k_similituds[i][1]*(self._score._mat[self._score._ll_usuaris.index(usuari)][self._score._ll_items.index(item)]-mitjana)
                    denominador+=k_similituds[i][1]
                puntuacio=numerador/denominador
                puntuacions.append((item, mitjana_usu+puntuacio))

        puntuacions.sort(key=lambda x: x[1], reverse=True)
        j=int(input("Quantes recomenacions vols?: "))
        i=0
        for i in range(j):
            return puntuacions[i][0]
            

        





        
        



        
    

        
