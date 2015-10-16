#!/usr/bin/python
# coding: utf-8

__author__ = "leo"
__date__ = "12/05/2014"

class MiError(Exception):
    def __init__(self, valor):
        self.valor = valor
        
    def __str__(self):
        return "Error: " + str(self.valor)

if __name__ == "__main__":
    """Módulo de prueba para una Excepción definida por el usuario"""
    
    try:
        valor = input("Ingrese un número:")
        if valor > 0:
            raise MiError("Ingresó un número positivo!")
    except MiError, e:
        print e
        
    print("Programa finalizado")