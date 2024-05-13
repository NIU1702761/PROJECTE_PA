#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:24:41 2024

@author: aliciamartilopez
"""

class User():
    
    _ID_user: str 
    _location: str
    _age: float
    
    def __init__(self, id_user, location, age):
        self._ID_user = id_user
        self._location = location
        self._age = age
        
    def __str__(self):
        resposta = ''
        resposta += 'ID: '+self._id_user+'\n'
        resposta += 'LOCALITAT: '+self._location+'\n'
        resposta += 'EDAT: '+self._age+'\n'
        return resposta