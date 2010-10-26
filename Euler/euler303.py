#! -*- coding: utf8 -*-
#Esta Aproximación del problema es realmente mala!
def is_target(x):
    flag = True
    for n in str(x):
        if int(n) > 2:
            flag = False
            break
    return flag

def function(x, n=1):
    while True:
        print n
        if is_target(x*n):
            return n, n*x
        n += 1
        
#print function(89)[1] == 1121222
#s = 0
#for n in xrange(1, 10001):
#    s += function(n)[0]
#    print n, s
#
#print "Resultado", s

"""
Idea 2: Creamos un **generador con cache** 
Los numeros que necesitamos son numeros en base ternaria.
como los numeros en base

"""
from progressbar import *

def ternary_number(index):
    div, module = divmod(index,3)
    s_num = str(module)
    while div:
        div, module = divmod(div, 3)
        s_num = str(module) + s_num
    
    return int(s_num)
print "Generando"
a = []
prog = ProgressBar(maxval=8000000).start()
for b in xrange(1, 8000000):
    a.append(ternary_number(b))
    prog.update(b+1)
print ''
print "generados"
print a[-1], len(str(a[-1]))
contador = 0
contador2 = 0
suma = 0
prog = ProgressBar(maxval=10001).start()
for m in xrange(1, 9999):

    for n in a:
        contador2 += 1
        bandera = True
        if not n%m:
            contador += 1
            suma += n/m
            bandera = False
            break
    if bandera:
        q = len(a)
        print "Numero malo: %d" %m
        while n%m:
            q += 1
            n = ternary_number(q)
        contador += 1
        suma += n/m
    
    prog.update(m+1)
print 'ahora vamos con el malo!'
numero = 11112222222222222222
suma += numero/9999
suma += 1
contador +=2
contador2 +=2
print ''
print contador == contador2
print contador, contador2
print contador == 10000
print suma 

