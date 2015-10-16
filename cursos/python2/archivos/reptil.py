#!/usr/bin/python
# coding: utf-8

class Reptil:
    """Abstracción de los objetos Reptil"""
    def __init__(self, tipo):
        self.tipo = tipo
        print("Yo soy un reptil: {tipo}").format(tipo=tipo)
        
    def avanzar(self):
        print("-{tipo}: Yo avanzo reptando!").format(tipo=self.tipo)