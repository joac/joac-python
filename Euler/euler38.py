"""Chequear que  un numero es pandigital"""

def is_pandigital(number):
    if len(str(number)) > 9: 
        return False
    check = set([1,2,3,4,5,6,7,8,9])
    set_n = set([int(a) for a in str(number)])
    return set_n == check

print is_pandigital(123456789)

lista = []

for number in xrange( 0, 50001):
    n = 2
    s_num = str(number)
    while len(s_num) < 9:
        s_num += str(number*n)
        n+=1
    if is_pandigital(int(s_num)):
        lista.append(int(s_num))
    
print sorted(lista)[-1]
