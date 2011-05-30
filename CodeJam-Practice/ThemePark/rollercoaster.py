#! -*- coding: utf8 -*-
def calc_money(cycles, max_pax, pax_queue):
    cash_box = 0
    idx_p = 0
    queue_len = len(pax_queue) - 1
    memo_dict = {}
    for n in xrange(0, cycles):
        free_seat = max_pax
        limit = 0
        
        if idx_p in memo_dict.keys():
            # en la primera coincidencia sabemos el largo del ciclo!
            cash_box *= (cycles / len(memo_dict.keys()))
            sys.stderr.write("%d -" % (cycles / len(memo_dict.keys())))
            for m in xrange(0, cycles % len( memo_dict.keys())):
                tuple_data = memo_dict[idx_p]
                cash_box += tuple_data[1]
                idx_p = tuple_data[0]
            break

        else:
            start = idx_p
            while ( limit <= queue_len and free_seat >= pax_queue[idx_p]):
                free_seat -= pax_queue[idx_p]
                limit += 1
                if idx_p < queue_len:
                    idx_p += 1
                else:
                    idx_p = 0
            money = (max_pax - free_seat)
            memo_dict[start] = (idx_p, money)
            cash_box += money
    
    return cash_box

if __name__ == '__main__':
    import sys
    fh = open(sys.argv[1])
    lines = fh.readlines()
    fh.close()

    cases = int(lines.pop(0))

    for case in xrange(1, cases+1):
        cycles, max_pax, groups = [int(n) for n in lines.pop(0).split()]
        pax_queue = [int(g) for g in lines.pop(0).split()]

        print "Case #%d: %d" % ( case, calc_money(cycles, max_pax, pax_queue))


    


