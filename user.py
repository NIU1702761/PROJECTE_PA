#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:24:41 2024

@author: aliciamartilopez
"""

class User():
    
    _ID_user: str 
    
    def __init__(self, id_user):
        self._ID_user = id_user
        
    def __str__(self):
        resposta = ''
        resposta += 'ID: '+self._id_user+'\n'
        return resposta
    