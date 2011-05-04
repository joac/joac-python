#! -*- coding: utf8 -*-

import sys

def check_snaps(snappers, snaps):
    chain_num = 2**snappers - 1
    return ((chain_num & snaps) == chain_num) and 'ON' or 'OFF'

if __name__ == '__main__':
    file = sys.argv[1]
    fh = open(file)
    lines = fh.readlines()
    fh.close()
    cases = int(lines.pop(0))
    for n in xrange(0, cases):
        a, b = [int(c) for c in lines.pop(0).split(' ')]
        print 'Case #%d: %s' % ( n+1, check_snaps(a, b))
    





