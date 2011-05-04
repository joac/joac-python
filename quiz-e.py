a = open('e-quiz.txt')
contador = 0
for n in a.readlines():
    n = n.replace('\n', '')
    cons_ok = True
    for q in xrange(0, 5):
            if n[q] == n[q+1]: 
                cons_ok = False
                break
    #calculamos la suma
    suma = 0
    for l in n:
        suma += int(l)
    if suma%2 == 0 and n[0] != n[-1] and cons_ok:
        contador +=1
print contador


