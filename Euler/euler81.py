#! -*- coding: utf8 -*-

"""
Queremos crear un solver de caminos de sumas minimos
La idea es parecida a otro problemas de project euler
(el de encontrar la minima suma en un triangulo...)
La clave esta encontrar la suma minima de cada linea diagonal...
Por Ejemplo:
------------
La matriz

1 2 3 4 
6 7 8 9
9 8 7 6
5 4 3 2

La matriz de sumas minimas

1--3  6  10
7  10-14 19
16 18 21 25
21 22 24-26


00 10 20 30
01 11 21 31
02 12 22 32
03 13 23 33

00 01 10 02 11 20 03 12 21 30 13 22 31 33

responde a la forma:
"""


#matriz =[
#        [1, 2, 3, 4],
#        [6, 7, 8, 9],
#        [9, 8, 7, 6],
#        [5, 4, 3, 2],
#        ]
a = [[int(b) for b in n.replace('\r\n', '').split(',')] for n in open('matrix.txt.1').readlines()]
matriz = a
n, m = len(matriz[1]) -1 , len(matriz)-1

for b in xrange(0, n+m+1):
    for a in xrange(0, b+1):
        x, y = b-a, a
        if x <= n and y <= m:
            q = matriz
            if (x, y) == (0, 0):
                pass
            elif x == 0:
                q[y][x] += q[y-1][x]
            elif y == 0:
                q[y][x] += q[y][x-1]
            else:
                q[y][x] += min(q[y][x-1], q[y-1][x])

print q[m][n]

