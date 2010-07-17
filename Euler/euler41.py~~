import itertools

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
    
pandigitalPrime = []
source = '123456789'
for a in range(1, 10):
    num = source[0:a]
    permutations = [int(''.join(a)) for a in itertools.permutations(num, len(num))]
    for n in permutations:
        if sumaDivisoresPropios(n) == 1:
            pandigitalPrime.append(n)

pandigitalPrime.sort()

print pandigitalPrime[-1]
