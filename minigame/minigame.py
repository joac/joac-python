#! /usr/bin/python
#!-*-coding: utf8-*-
import random
import os
import time
import copy
class Square:
    """This is the abstraction of one Square"""
    def __init__(self, x, y, attrib):
        self.x = x
        self.y = y
        self.attrib = attrib
        self.rep = '\033[4%sm%s \033[0m' % (attrib, attrib)
        self.have_vecinos = True
        self.is_child = False
class Screen:
    """The Screen Array of the game"""
    def __init__(self, x_size, y_size, tokens):
        self.x_size = x_size
        self.y_size = y_size
        self.tokens = tokens
        self.childs = []
        self.squares = []
        self.populate()
        self.childs.append(self.squares[0][0])
        self.childs[0].rep = '# '
        self.childs[0].is_child = True
        self.attrib = self.childs[0].attrib
    def get_near_to(self, child):
        vecinos = []
        if child.x - 1 >= 0:
            vecinos.append(self.get_square(child.x - 1, child.y))
        if child.y - 1 >= 0:
            vecinos.append(self.get_square(child.x, child.y - 1))
        if child.x + 1 < self.x_size:
            vecinos.append(self.get_square(child.x +1, child.y))
        if child.y + 1 < self.y_size:
            vecinos.append(self.get_square(child.x, child.y + 1))
        vecinos = [vecino for vecino in vecinos if(not vecino.is_child)]
        if not vecinos:
            child.have_vecinos = False
        return vecinos
    def get_square(self, x, y):
        return self.squares[y][x]
    def populate(self):
        for y in xrange(0, self.y_size):
            self.squares.append([self.random_square(x, y) for x in xrange(0, self.x_size)])
    def random_square(self, x, y):
        attrib = random.choice(self.tokens)
        square = Square(x, y, attrib)
        return square
    def check_arround(self, child):
        """We check the attrib of the near squares"""
        vecinos = self.get_near_to(child)
        if vecinos:
            for vecino in vecinos:
                if (vecino.attrib == self.attrib):
                    vecino.rep = child.rep
                    self.childs.append(vecino)
                    vecino.is_child = True
    def __repr__(self):
        output = ''
        for row in self.squares:
            output += ''.join(['%s' % str(a.rep) for a in row])
            output += '\n'
        return output
    def update(self, attrib):
        self.attrib = attrib[0]
        for child in self.childs:
            if child.have_vecinos:
                self.check_arround(child)
class Solver(Screen):
    """Toma un Puzzle y lo resuelve de manera optima"""
    def __init__(self, puzzle):
        self.squares = puzzle.squares
        self.tokens = puzzle.tokens
        self.childs = []
        self.x_size = puzzle.x_size
        self.y_size = puzzle.y_size
        self.attrib = puzzle.attrib
    def solve(self):
        """Resuelvo un puzzle, para saber cuantos movimientos son necesarios"""
        for a in self.tokens:
            pass
    def check_move(token):
        """Chequea cuantos cuadraditos agrega una eleccion de token"""
        hijos = copy.copy(self.childs)
    def my_check_arround(self, child, childlist):
        """We check the attrib of the near squares"""
        vecinos = self.get_near_to(child)
        if vecinos:
            for vecino in vecinos:
                if (vecino.attrib == self.attrib):
                    vecino.rep = child.rep
                    childlist.append(vecino)
                    vecino.is_child = True
if __name__ == '__main__':
    os.system('clear')
    tokens = [str(d) for d in xrange(1, 9)]
    screen = Screen(20, 20, tokens)
    print(screen)
    screen.update(screen.childs[0].attrib) #dirty Hack
    limit = screen.x_size + screen.y_size 
    win = False
    for b in xrange(1, limit + 1):
        time.sleep(0.5)   
        a = raw_input('_#: ')
        screen.update(a)
        os.system('clear')
        print(screen)
        print(f'{b}moves of {limit}')
        if len(screen.childs) == screen.x_size*screen.y_size:
            win = True
            break
    if win:
        print("You Win")
    else:
        print("You loose")
