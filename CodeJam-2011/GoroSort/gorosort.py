#! -*- coding: utf8 -*-

def calc_sort_steps(list_a):
    """calc sort steps using optimal strategy"""
    count = 0
    for n, element in enumerate(list_a, 1):
        if n != element:
            idx = list_a.index(n)
            list_a[idx] = element
            list_a[n-1] = n
            count += 2.0
    return count

if __name__ == '__main__':
    import sys

    fh = open(sys.argv[1])
    lines = fh.readlines()
    fh.close()

    cases = int(lines.pop(0))

    for case in xrange(1, cases + 1):
        array_len = int(lines.pop(0))
        array = [int(n) for n in lines.pop(0).split()]
        result = calc_sort_steps(array[:array_len])
        print "Case #%d: %.6f %s" %(case, result, str(array))




