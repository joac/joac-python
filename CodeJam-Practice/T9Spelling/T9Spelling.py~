import sys

def main(input):
    trans_table = { 'a':'2', 'b':'22', 'c':'222',
                    'd':'3', 'e':'33', 'f':'333',
                    'g':'4', 'h':'44', 'i':'444',
                    'j':'5', 'k':'55', 'l':'555',
                    'm':'6', 'n':'66', 'o':'666',
                    'p':'7', 'q':'77', 'r':'777', 's':'7777',
                    't':'8', 'u':'88', 'v':'888',
                    'w':'9', 'x':'99', 'y':'999', 'z':'9999',
                    ' ':'0',}

    cases = int(input.pop(0))
    for case in xrange(1, cases+1):
        text = input.pop(0)
        output = ''
        previous = ''
        for n in xrange(0, len(text)-1):
            character = trans_table[text[n]]
            if previous and previous[0] == character[0]:
                output += ' ' + character
            else:
                output += character
            previous = character

        print "Case #%d: %s" %(case, output)





if __name__ == "__main__":

    try:
        input = open(sys.argv[1]).readlines()
    except:
        input = ["4", "hi", "yes", "foo  bar", "hello world"]
    main(input)
