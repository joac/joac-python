import math
def sumaDivisoresPropios(numero):
    n = numero
    p =2
    sum = 1
    while pow(p, 2) <= n and n >1:
        if not n%p:
            j = pow(p,2)
            n /= p
            while not n%p:
                j *= p
                n /= p
            sum *= (j-1)
            sum /= (p-1)
        if p == 2: p = 3
        else: p +=2
    if n>1: sum *=(n+1)
    sumaDivisor = sum - numero    
    return sumaDivisor
    
abundantes = []
for a in xrange(12, 28123):
    if sumaDivisoresPropios(a) > a:
        abundantes.append(a)
print abundantes[0:5]
#print abundantes, len(abundantes)

dosAbundante = set([])

for a in abundantes:
    for b in abundantes:
        valor = a+b
        if valor < 28123:
            dosAbundante.add(a+b)
print len(dosAbundante)
total = 0
for n in dosAbundante:
    total += n 
superior = 0
for n in xrange(1, 28123):
    superior += n
print superior
print total
print (superior-total)

