numbers = []

for n in xrange(1, 1000):
    a = 1
    cicle = []
    while True:
        a %= n
        a *= 10
        print a
        if a:
            if a not in cicle:
                cicle.append(a)
            else:
                cicle = cicle[cicle.index(a):]
                large = len (cicle)
                numbers.append((large, n))
                break
        else: break
    

numbers.sort()
print numbers
print numbers[-1]

