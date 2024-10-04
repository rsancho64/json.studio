#! /usr/bin/python3

x = 22
y = 33

def produce(entrada):
    """funcion pura"""
    nuevo = entrada + 1
    return nuevo

def cambia(entradaYSalida):
    entradaYSalida = entradaYSalida + 1

def mixed(entrada,salida):
    intermedio = entrada + 1
    salida = intermedio

if __name__ == "__main__":

    print(x)
    print(y)

    producto = produce(x)
    print(producto)