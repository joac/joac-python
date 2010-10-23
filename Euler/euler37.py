def es_primo(numero):
    if numero == 2:
        return True
    if numero == 1 or not numero%2:
        return False
    for n in xrange(3, numero, 2):
        if not numero%n: 
            return False
    return True

def es_primeable(numero):
    s_numero = str(numero)
    for n in xrange(1, len(s_numero) ):
        tail = int(s_numero[:-n])
        print tail
        head = int(s_numero[n:])
        print head
        if not es_primo(tail): return False
        if not es_primo(head): return False
    return True

listado = []
numero = 11
print es_primeable(23)
print es_primeable(3797)
#exit()
while len(listado)<11:
    s_numero = str(numero)
    cola, head = int(s_numero[-1]),int( s_numero[0])
    if cola in [3, 7] and head in [2, 3, 5, 7]:
        if es_primo(numero):
            if es_primeable(numero):
                listado.append(numero)
                print listado
    numero += 2
    print numero


