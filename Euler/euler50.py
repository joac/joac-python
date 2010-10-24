#! -*- coding: utf8 -*-
"""
Vamos a calcular el maximo primo que se puede obtener como suma de
primos consecutivos. 
Para ello vamos a utilizar una criba de eratostenes
"""
def calcSieve(limit):
    sievebound = limit + 1
    sieve = [True]*sievebound
    sieve[0] = sieve [1] = False
    candidate = 2
    while candidate < sievebound:    
        if sieve[candidate]:
            for j in xrange(candidate*2, sievebound, candidate):
                sieve[j] = False
        candidate += 1        
    return [n for n in xrange(2, sievebound) if sieve[n]], sieve

def main(limit = 1000000):
    primes, sieve = calcSieve(limit)
    # una idea... empezar a sumar desde el primer primo
    # hasta que supere el millón
    # Si tenemos algun hit, lo metemos en nuestra lista de tuplas (cantidad de primos, primo)
    # cuando supera el millón, quitamos el primer primo y volvemos a empezar
    primos = []
    while len(primes) > 1:
        suma = 0
        for n, prime in enumerate(primes):
            suma += prime
            if suma > limit:
                primes = primes[1:]
                break
            elif sieve[suma]:
                primos.append((n+1, suma))
    primos.sort()
    print primos[-1]

if __name__ == '__main__':
    import sys
    if sys.argv[1]:
        atr = int(sys.argv[1])
    else:
        atr = 100

    main(atr)

