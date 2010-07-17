import sys

def mach_group(string):
    char_list = [n for n in string]
    groupes = []
    while len(char_list):
        group =[]
        a = char_list.pop(0)
        if a == '(':
           b=char_list.pop(0)
           while b!=')':
               group.append(b)
               b = char_list.pop(0)
           groupes.append(group)
        else: groupes.append(a)
    return groupes

def main(input):
    words_len, words_num, cases_num = [int(a) for a in input.pop(0).split() ]
    
    print "Case #%d: %s" %(case, output)





if __name__ == "__main__":

    try:
        input = open(sys.argv[1]).readlines()
    except:
        input = ["3 5 4", "abc", "bca", "dac", "dbc", "cba", "(ab)(bc)(ca)","abc", "(abc)(abc)(abc)", "(zyx)bc"]
    
    main(input)
