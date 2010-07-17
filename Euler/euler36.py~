def reversed(a):
   a = [b for b in a]
   a.reverse()
   return ''.join(a)

total = 0
for a in xrange(1, 1000000):
    adecstring = str(a)
    abinstring = str(bin(a))[2:]
    print adecstring, abinstring
    if (adecstring == reversed(adecstring))and(abinstring == reversed(abinstring)): total += a

print total    
    
