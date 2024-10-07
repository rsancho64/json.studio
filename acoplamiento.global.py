#! /usr/bin/python3

global x 
x = 22
y = 33

def produce(entrada):
    """funcion pura"""
    nuevo = entrada + 1
    return nuevo

def cambia():
    """procedimiento puro"""
    global x
    x = x + 1
    return

def mixed(entrada,salida):
    intermedio = entrada + 1
    salida = intermedio

if __name__ == "__main__":

    # print(x) # estado global a 22

    # producto = produce(x)
    # print(producto)
    
    # print(x) # estado global a 22

    # x = produce(x)
    # print(x) # estado global a 23

    print(x) # 22 antes
    cambia()  # PROCEDIMIENTO
    print(x) # 23 despues
   