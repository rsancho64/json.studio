#! /usr/bin/python3

"""estudio de json como fomato para seralizar objetos py
    v0: disciplina de pila en el contenedor
"""
import json


class Jsonable:

    __data = []

    def __init__(self):
        __data = []

    def __str__(self) -> str:
        return (str(self.__data))

    def push(self, algo) -> None: 
        self.__data.append(algo)

    # exceptions: try, throw, catch, exception ....

    # pop() falible en IndexError de la <class list>.pop()
    # def pop(self) -> object:
    #         return self.__data.pop()

    # pop() que tolera el fallo <class list>.pop() de estado vacio 
    # reconociendolo por si mismo.
    # def pop(self) -> object:
    #     if 0 == len(self.__data):  # lazy way of life
    #         return None
    #     else:
    #         return self.__data.pop()

    # pop() que tolera el fallo <class list>.pop() de estado vacio 
    # delegando su reconocimiento (a la <class list>) y menajandolo.
    def pop(self) -> object:
        try:
            return self.__data.pop()
        except IndexError:
            return None

    def dumpJson(self) -> str :
        # return json.dumps(self.__data)
        return json.dumps(self.__data, sort_keys=True, indent=3)

    def loadJson(self, ajson) -> None :
        self.__data = json.loads(ajson)

if __name__ == "__main__":

    js0 = Jsonable()
    print(js0)

    js0.push("patata")
    print(js0)

    js0.push("cebolla")
    print(js0)

    js0.push("huevos")
    print(js0)

    print(js0.dumpJson())

    algo = js0.pop()
    print(js0, algo)

    algo = js0.pop()
    print(js0, algo)

    algo = js0.pop()
    print(js0, algo)

    algo = js0.pop()
    print(js0, algo)

    js0.loadJson('["foo", {"bar":["baz", null, 1.0, 2]}]')
    print(js0)
    print(js0.dumpJson())

