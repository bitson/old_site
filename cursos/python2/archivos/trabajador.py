#!/usr/bin/python
# coding: utf-8

__author__ = "leo"
__date__ = "12/05/2014"

class Trabajador:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def trabajar(self):
        print("-{name}: Trabajo muy duro! Como un esclavo!").format(name=self.nombre)


class Jubilado(Trabajador):
    def trabajar(self):
        print("-{name}: Ya no trabajo! Soy JUBILADO!!").format(name=self.nombre)


class Menor(Trabajador):
    def trabajar(self):
        print("-{name}: EXPLOTADOR!!!!").format(name=self.nombre)
        
        
if __name__ == "__main__":
    """Esta es una prueba de la clase trabajador"""
    homero = Trabajador("Homero Simpson")
    homero.trabajar()
    
    abuelo = Jubilado("Abraham Simpson")
    abuelo.trabajar()
    
    bart = Menor("Bart Simpson")
    bart.trabajar()