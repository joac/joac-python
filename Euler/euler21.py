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
def main():
    sumaPares = 0
    for numero in xrange(2, 10000):
        amigable = sumaDivisoresPropios(numero)
        if amigable > numero and sumaDivisoresPropios(amigable) == numero:
            sumaPares += (numero + amigable)
            
    print 'La suma es: %d ' %(sumaPares)

if __name__ == '__main__':
    main()
