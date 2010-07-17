pos = 0
for pound_2 in range(0, 201, 200): #dos libras
    for pound_1 in xrange(0, 201, 100): # una libra
        if pound_2+pound_1 > 200:
            break
        for pence_50 in xrange(0,201 , 50): #50chelines
            if pound_2+pound_1+pence_50 >200:
                break
            for pence_20 in xrange(0, 201, 20 ):
                
                if pound_2+pound_1+pence_50+pence_20 > 200:
                    break
                for pence_10 in xrange(0, 201, 10):
                    sum = pound_2+pound_1+pence_50+pence_20+pence_10
                    if sum >200:
                        break
                    for pence_5 in xrange(0,201, 5):
                        sum = pound_2+pound_1+pence_50+pence_20+pence_10+pence_5
                        if sum > 200:
                            break
                        for pence_2 in xrange(0,201, 2):
                            sum = pound_2+pound_1+pence_50+pence_20+pence_10+pence_5+pence_2
                            if sum > 200:
                                break
                            for pence in xrange(0,201):
                                sum = pound_2+pound_1+pence_50+pence_20+pence_10+pence_5+pence_2+pence
                                if sum == 200:
                                    pos += 1
                                    break

print pos
