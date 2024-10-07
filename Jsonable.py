#! /usr/bin/python3

"""estudio de json como fomato para seralizar objetos py
    v0: disciplina de pila en el contenedor
"""


class Jsonable:

    __data = []

    def __init__(self):
        __data = []

    def __str__(self) -> str:
        return (str(self.__data))

    def push(self, algo) -> None: 
        self.__data.append(algo)

    def pop(self) -> object:
        return self.__data.pop()
if __name__ == "__main__":

    js0 = Jsonable()
    print(js0)

    js0.push("patata")
    print(js0)

    js0.push("cebolla")
    print(js0)

    js0.push("huevos")
    print(js0)

    algo = js0.pop()
    print(js0, algo)

    algo = js0.pop()
    print(js0, algo)

    algo = js0.pop()
    print(js0, algo)

    algo = js0.pop()
    print(js0, algo)




