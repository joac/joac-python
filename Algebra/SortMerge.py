#! -*- coding: utf8 -*-
import collections

def my_merge(lista1, lista2):
    """une dos listas ordenadas"""
    lista1 = collections.deque(lista1)
    lista2 = collections.deque(lista2)
    merged = collections.deque()
    while lista1  and lista2:
        if lista1[0] <= lista2[0]:
            merged.append(lista1.popleft())
        elif lista1[0] > lista2[0]:
            merged.append(lista2.popleft())
    if lista1:
        merged.extend(lista1)
    if lista2:
        merged.extend(lista2)
    return list(merged)

def my_sort(lista):
    """Ordena Una lista usando el algoritmo recursivo SortMerge"""
    largo = len(lista)
    if largo > 1:
        return my_merge(my_sort(lista[:largo/2]), my_sort(lista[largo/2:]))
    else:
        return lista




def run():    
    import random
    from processing import Pool

    p=Pool(2)

    print "ahora vemos si escala"
 
    numero = 5000000
    a = [random.randint(0, 100) for a in xrange(0, numero)]
    
    print "Ya tenemos los numeros"
    lista = [a[:numero/2] , a[numero/2:]]
    print "Lista bisectada"
    result=p.mapAsync(my_sort, lista)
    print "threads lanzados"
    lista1, lista2 = result.get()
    print "Uniendo listas"
    b = my_merge(lista1, lista2)
   # b = my_sort(a)
    print "largo", len(b), "llamadas a my_sort"
    # a = [u"ernesto", u"zamudio", u"roberto", u"inocencio", u"trifulco", u"zoilo", u"andres"]
   # print my_sort(a)

if __name__ == "__main__":
   run()
   # import profile 
   # profile.run("run()", filename="profile_Sortmerge.txt")
