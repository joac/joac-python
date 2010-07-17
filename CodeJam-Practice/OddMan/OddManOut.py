import sys



def main(input):
    result = []
    cases = int(input[0])
    for case in xrange(1, cases+1):
        input.pop(1)
        keys = [int(key) for key in input.pop(1).split()]
        unique = [a for a in keys if keys.count(a)==1]
        print "Case #%d: %d" %(case, unique[0])

if __name__ == "__main__":

    try:
        input = open(sys.argv[1]).readlines()
    except:
        input = ["3", "3", "1 2147483647 2147483647", "5", "3 4 7 4 3", "5", "2 10 2 10 5"]
    main(input)
