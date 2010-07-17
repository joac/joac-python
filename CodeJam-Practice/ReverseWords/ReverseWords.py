import sys

def main(input):
    cases = int(input.pop(0))
    for case in xrange(1, cases+1):
        text = input.pop(0)
        reverse = ' '.join(reversed(text.split()))
        print "Case #%d: %s" %(case, reverse)





if __name__ == "__main__":

    try:
        input = open(sys.argv[1]).readlines()
    except:
        input = ["3", "this is a test", "foobar", "all your base"]
    main(input)
