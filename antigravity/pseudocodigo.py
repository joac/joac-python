#! -*- coding: utf8 -*-

#Pseudo Codigo para el juego antigravity
#

class Masa(object):
    """
    Es la clase base para todos los objetos del juego
    define las propiedades basicas
    """
    def __init__(self, x, y, masa):
        self.x = x
        self.y = y
        self.masa = masa

    def get_posicion(self):
        return self.x , self.y

class Masa

