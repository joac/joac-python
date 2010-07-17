numero = ''
total = 1
for n in xrange(0, 1000000):
    numero += (str(n))
    if len(numero) > 1000000:
        print 'llegamos hasta %d' % n
        break
for a in xrange(0, 7):
    total *= int(numero[pow(10, a)])

print total

