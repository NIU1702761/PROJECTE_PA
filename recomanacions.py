from score import Score
from item import Item, Book, Movie
from user import User
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
import csv

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
    
    #def recomanacio_colaborativa(self):
        #return items=[]
    
    def recomanacio_basada_en_contingut(self, fitxer_generes_pelis):
        item_features = []
        with open(fitxer_generes_pelis, 'r') as f:
            next(f)
            reader = csv.reader(f)
            for line in reader:
                generes = line[-1]
                item_features.append(generes)
        
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(item_features).toarray()
        
        print (" Vocabulary : {}".format(tfidf.get_feature_names_out())) 
        print (" Shape : {}".format(tfidf_matrix.shape))
        
        vector_puntuacions = self._score.vector_puntuacions(self._id_user)
        print("Shape vector_puntuacions: {}".format(vector_puntuacions.shape))
        
        #vector_puntuacions_flat = np.ravel(vector_puntuacions)
        #mat_numerador = np.repeat(vector_puntuacions, 2, axis = 1) * tfidf_matrix

        #mat_numerador = np.outer(vector_puntuacions, tfidf_matrix)
        mat_numerador = vector_puntuacions * tfidf_matrix 
        print (" Shape mat_mumerador: {}".format(mat_numerador.shape))
        perfil_user = np.sum(mat_numerador, axis=0)
        valor_normalitzador = np.sum(vector_puntuacions)
        
        Q = perfil_user / valor_normalitzador
        print (" Shape Q: {}".format(Q.shape))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        