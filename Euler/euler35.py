import math
def calcPrimes(limit):
   
    sievebound = limit + 1
    sieve = [True]*sievebound
    sieve[0] = sieve [1] = False
    candidate = 2
    while candidate < sievebound:    
        if sieve[candidate]:
            for j in xrange(candidate*2, sievebound, candidate):
                sieve[j] = False
        candidate += 1        
    return sieve 

def rotar(num):
    num = str(num)
    rotations = []
    dist = len(num)
    cop = num*2
    for n in xrange( 0, dist):
        rotations.append(int(cop[n:dist+n]))
    return rotations

def main():
    circular = 0 
    lista = []
    limit = 1000000
    sieve = calcPrimes(limit)
    circulares = []    
    for n in xrange(2, limit): 
        if sieve[n]:
            rotaciones = rotar(n)
            lista =[n for n in rotaciones if sieve[n]]
            if lista == rotaciones:
                circular += 1
                circulares.append(n)
    
    print circular
    print circulares

if __name__ == '__main__':
    main()

        
