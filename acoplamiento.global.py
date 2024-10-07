#! /usr/bin/python3

global x 
x = 22

def sube():
    """procedimiento puro"""
    global x
    x = x + 1
    return

def baja():
    """procedimiento puro"""
    global x
    x = x - 1
    return

if __name__ == "__main__":

    print(x)
    sube()
    sube()
    sube()
    baja()
    sube()
    print(x)

   