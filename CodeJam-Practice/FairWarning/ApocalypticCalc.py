#! -*- coding: utf8 -*-

#idea de algoritmo
# calcular la distancia entre dos eventos consecutivos
# calcular el mcd entre las distancias
# sumarle el mcd a las distancias
# chequear que 

def mcd(a, b):
    """Calcula el mcd entre dos numeros"""
    if b == 0:
        return a
    return mcd(b, a%b)

def check_apocalypse(y, delta, checklist ):
    for n in checklist:
        if ((n+y) % delta):
            return False
            break
    return True

def calc_apocalypse(event_string):
    """Calcula la fecha del apocalipsis"""
    #creamos la lista de distancias
    data_list = event_string.split()

    cases = int(data_list.pop(0))

    event_list = [int(data_list.pop(0)) for n in xrange(0, cases)]

    event_list.sort() 
    first = event_list[0]
    
    date_distance = [abs(event - first) for event in event_list]
    
    delta = reduce(mcd, date_distance)
    if first % delta == 0:
        return 0
    y = delta - (first % delta)
    return y





if __name__ == '__main__':
    import sys
    fh = open(sys.argv[1])
    lines = fh.readlines()
    fh.close()

    cases = int(lines.pop(0))
    
    for n in xrange(0, cases):
        delta = calc_apocalypse(lines.pop(0))
        print "Case #%d: %d" % (n+1, delta)
