def s_digits(num):
    a = list(str(num))
    a.sort()
    return a

numero = 1
while True:
    dig_num = s_digits(numero)
    is_target = True
    for n in xrange(1, 7):
        if s_digits(numero*n) != dig_num:
            is_target = False
            break
    if is_target:
        print numero
        break
    else:
        numero += 1

