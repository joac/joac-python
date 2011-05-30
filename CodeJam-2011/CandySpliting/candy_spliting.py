#! -*- coding: utf8 -*-
import operator
#sean pretende tener mas caramelos que patrick

#chequear que la suma %2 de cero

def calc_max_candy(candy_list):
    
    #check if is possible to split the candy
    
    if reduce(operator.xor, candy_list) == 0:
        candy_list.sort()
        return str(sum(candy_list) - min(candy_list))
    else:
        return 'NO'

if __name__ == '__main__':
    import sys

    fh = open(sys.argv[1])
    lines = fh.readlines()
    fh.close()

    cases = int(lines.pop(0))
    
    for case in xrange(1, cases + 1):
        candy_len = int(lines.pop(0))
        candy_list = [int(n) for n in lines.pop(0).split()]
        result = calc_max_candy(candy_list[:candy_len])
        print "Case #%d: %s" % (case, result)


