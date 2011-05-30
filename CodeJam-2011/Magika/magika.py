#! -*- coding: utf8 -*-

def calc_magika(line):
    comb_dict = {}
    op_list = []
    
    line = line[:-1].split() #remove te \n
    
    comb = int(line.pop(0))
    
    if comb:
        for n in xrange(0, comb):
            a = line.pop(0)
            comb_dict[tuple(sorted(a[:2]))] = a[-1]
    
    op = int(line.pop(0))
    if op:
        for n in xrange(0, op):
            a = line.pop(0)
            op_list.append(tuple(sorted(a)))

    elements = ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f']
    
    elem_list = []
    inv_len = int(line.pop(0))
    invocation = line.pop(0) 
    invocation = invocation[:inv_len]
    
    for element in invocation:
    
        elem_list.append(element)
        if len(elem_list) >= 2:
            last_elems = tuple( sorted(elem_list[-2:]) )
            
            if last_elems in comb_dict.keys():
                elem_list = elem_list[:-2]
                elem_list.append(comb_dict[last_elems])
            
        if len(elem_list) >= 2:
            for a, b in op_list:
                if a in elem_list and b in elem_list:
                    elem_list = []
    
    return '[' + ', '.join(elem_list) +']'

if __name__ == '__main__':
    import sys
    fh = open(sys.argv[1])
    lines = fh.readlines()
    fh.close()

    cases = int(lines.pop(0))
    
    for case in xrange(1, cases +1):
        a = lines.pop(0)
        print "Case #%d: %s" % (case, calc_magika( a ))
