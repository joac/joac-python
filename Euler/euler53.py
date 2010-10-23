#! -*- coding: utf8 -*-
import math

def Combinatorio_x(n):
    """Calculamos el numero combinatorio utilizando el triangulo de pascal
    calculamos la n-esima fila y la devolvemos"""
    current_row = [1]
    for n in xrange(1, n+1):
        temp_row = [1]
        for b in xrange(0, len(current_row) -1):
            temp_row.append(current_row[b]+current_row[b + 1])
        
        temp_row.append(1)
        current_row = temp_row
    return current_row


if __name__ == "__main__":
    hits = 0
    for n in xrange(1, 101):
        fila = Combinatorio_x(n)
        for a in fila:
            if a > 1000000:
                hits += 1
    print hits
