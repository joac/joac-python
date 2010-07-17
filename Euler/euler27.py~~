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
    return sieve 

def quadratic(a, b, n):
    return pow(n, 2)+a*n+b

expresions=[] 
sieve = calcSieve(1000000)
for a in  xrange(-999, 1000):
    for b in xrange(-999, 1000):
        n = 0
        while sieve[quadratic(a, b, n)]:
            n += 1
        expresions.append((n, a, b))

expresions.sort()
n, a, b = expresions[-1]
print a*b
        
