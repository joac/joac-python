import sys

def match(amount, items):
    _items = [a for a in enumerate(items) if a[1] < amount]
    for n in xrange(0, len(_items)):
        index_1, value_1 = _items[n]
        for m in xrange(n+1, len(_items)):
            index_2, value_2 = _items[m]
            total = value_1 + value_2
            if total == amount:
                return index_1+1, index_2+1

    


def main(input):
    cases = int(input.pop(0))
    for case in xrange(1, cases+1):
        amount = int(input.pop(0))
        n_items = int(input.pop(0))
        items = [int(a) for a in input.pop(0).split()]
        item_1, item_2 =  match(amount, items)
        print "Case #%d: %d %d" %(case, item_1, item_2)





if __name__ == "__main__":

    try:
        input = open(sys.argv[1]).readlines()
    except:
        input = ["3", "100", "3", "5 75 25", "200", "7", "150 24 79 50 88 345 3", "8", "8", "2 1 9 4 4 56 90 3"]
    main(input)
