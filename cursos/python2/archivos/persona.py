#!/usr/bin/python
# coding: utf-8

class Persona:
    """Abstracción de los objetos Persona"""
    def __init__(self, nombre):
        self.nombre = nombre
        print("Acabo de ser creado y me llamo {nombre}").format(nombre=nombre)

    def avanzar(self):
        print("Soy {nombre} y estoy caminando hacia adelante!").format(nombre=self.nombre)
