#! -*- coding: utf8 -*-
import math

def Combinatorio(n, m):
    """Calculamos el numero combinatorio utilizando el triangulo de pascal
    calculamos la n-esima fila y devolvemos el m-simo valor"""
    current_row = [1]
    for n in xrange(1, n+1):
        temp_row = [1]
        for b in xrange(0, len(current_row) -1):
            temp_row.append(current_row[b]+current_row[b + 1])
        
        temp_row.append(1)
        current_row = temp_row
    return current_row[m]


if __name__ == "__main__":
    comb = Combinatorio(100, 50)
    print "El combinatorio de n=100 m=50 es igual a: %d " % comb
    print "Lo testeamos"
    test = math.factorial(100)/(math.factorial(50)*math.factorial(100-50))
    print "Usando math.factorial da: %d" % test
    print "Son Iguales??", test == comb

