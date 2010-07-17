def fixedpow(base, expnt):
    cbase = base
    for n in xrange(1, expnt):
        cbase *= base
        s_base = str(cbase)
        if len(s_base)>2:
            cbase = int(s_base[-20:])
    return cbase

print str(28433*fixedpow(2, 7830457)+1)[-10:]


