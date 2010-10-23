"""Vamos a buscar todos los numeros de Lichrel por debajo de 10.000 """

def reverse(number):
    "devolvemos el reverso de un numero"
    return int(str(number)[::-1])

def is_palindrome(number):
    """Chequeamos que el numero sea un palindromo"""
    return number == reverse(number)
def lichrel_num(number, limit=50):
    number = number+reverse(number)
    if is_palindrome(number):
        return False
    elif limit:
        return lichrel_num(number, limit-1)
    else:
        return True

def main():
    print lichrel_num(196)
    numeros = 0
    for n in xrange(1, 10000):
        if lichrel_num(n): 
            numeros += 1
    print numeros        
if __name__ == '__main__':
    main()
