#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:41:57 2024

@author: aliciamartilopez
"""
import numpy as np
import math

class Avalua():
    
    def __init__(self, prediccions, puntuacions_originals):
        self._prediccions = prediccions
        self._puntuacions_originals = puntuacions_originals
    
    def MAE(self):
        numerador = abs(self._prediccions - self._puntuacions_originals)
        return np.sum(numerador)/len(numerador)
    
    def RMSE(self):
        numerador = (self._puntuacions_originals - self._prediccions)**2
        return math.sqrt(np.sum(numerador) /len(numerador))