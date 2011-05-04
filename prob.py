for a in xrange(0, 100000, 12):
    if not( a in [2*(n**2) for n in xrange(0, a/2)]):
            continue
    if not (a in [3*(n**3) for n in xrange(0, a/3)]):
            continue
    if not (a in [4*(n**5) for n in xrange(0, a/4)]):
            continue
    print a
    break

