#!/usr/bin/python
# coding: utf-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "leo"
__date__ = "$09/05/2014 11:06:50$"


class Encapsulamiento:
    def __init__(self):
        self.__atributo_privado = "este atributo es privado."
        self._atributo_semi_privado = "este atributo es \"casi\" privado."
        self.atributo_publico = "este atributo es público."

    def publico(self):
        return "Este es un método Público"

    def _semi_privado(self):
        return "Este es un método Semi Privado"

    def __privado(self):
        return "Este es un método Privado"

    def get_atributo_privado(self):
        return self.__atributo_privado

    def set_atributo_privado(self, valor):
        self.__atributo_privado = valor

    secreto = property(get_atributo_privado, set_atributo_privado)


if __name__ == "__main__":
    # Instanciamos un objeto de la clase Encapsulamiento
    objeto = Encapsulamiento()
    # Probamos el método público
    print("Probamos el método público:")
    print("\t" + objeto.publico())
    print("Probamos el método semi privado:")
    print("\t" + objeto._semi_privado())
    # Intentamos acceder al método privado
    #print("Intentamos acceder al método privado:")
    #print("\t".join(objeto.__privado()))
    # Al nombrar al método con el prefijo __ ocurre el "name mangling"
    # para acceder al método privado, (comentar la línea anterior):
    print("Accedemos al método privado (name mangling):")
    print("\t"+objeto._Encapsulamiento__privado())

    print('-'*30)
    # Accedemos al atributo público
    print("Imprimimos el atributo público:")
    print("\t" + objeto.atributo_publico)
    print("Imprimimos el atributo semi privado:")
    print("\t" + objeto._atributo_semi_privado)
    # Intentamos acceder al atributo privado
    #print("Intentamos acceder al atributo privado:")
    #print(objeto.__atributoPrivado)

    print('-'*30)
    # Utilizando los getters y setters:
    print("Obtenemos al atributo vía el getter:")
    print("\t" + objeto.get_atributo_privado())
    print("Cambiamos el atributo vía el setter:")
    objeto.set_atributo_privado("Cambiado a través del setter...")
    print("\t" + objeto.get_atributo_privado())

    print('-'*30)
    print("Usamos la propiedad:")
    objeto.secreto = "Cambiado a través de la propiedad"
    print("\t" + objeto.secreto)