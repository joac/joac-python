"""Vamos a calcular la minima clave para el banco!"""

logins = [a.replace('\r\n', '') for a in open('keylog.txt').readlines()]
numero = 100 
while True:
    s_numero = str(numero)
    is_number = True
    for login in logins:
        a, b, c = list(login)
        if not a in s_numero:
            is_number = False
            break
        if not b in s_numero[s_numero.index(a):]:
            is_number = False
            break
        if not c in s_numero[s_numero.index(b):]:
            is_number = False
            break
    if is_number:
        print numero
        break
    else:
        numero += 1
        print numero
    
