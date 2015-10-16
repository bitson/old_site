#!/usr/bin/python
# coding: utf-8

__author__ = "leo"
__date__ = "12/05/2014"

if __name__ == "__main__":
    """Se muestra el funcionamiento del bloque try-except"""
    
    print("Este programa te pide 2 números.")
    print("Si en el primer caso ingresás una letra, el programa se rompe.")
    print("Si en el segundo caso ingresás una letra, el programa continúa.")
    print("-"*40)
    
    variable = input("1° Caso) Ingrese un número: ")
    
    try:
        numero = input("2° Caso) Ingrese otro número: ")
    except Exception as e:
        print("Ha ocurrido un error: {excepcion}".format(excepcion=e))
    else:
        print("Usted ingresó los números {} y {}".format(variable, numero))
    finally:
        print("Se terminó el programa, limpiando...")