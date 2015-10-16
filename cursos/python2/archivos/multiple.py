#!/usr/bin/python
# coding: utf-8

__author__ = "leo"
__date__ = "12/05/2014"

import trabajador

class Persona:
    def __init__(self, edad):
        self.edad =  edad
        
    def trabajar(self):
        print("-Persona: tengo {age} años.").format(age=self.edad)
        

class Empleado(Persona, trabajador.Trabajador):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def identidad(self):
        print("Soy {name} y tengo {age} años").format(name=self.nombre, age=self.edad)
        
        
if __name__ == "__main__":
    """Una muestra de la herencia múltiple."""
    sujeto = Persona(32)
    sujeto.trabajar()
    
    programador = Empleado("Esteban", 24)
    programador.identidad()
    programador.trabajar()