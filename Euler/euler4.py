def checkpalindrome(foo):
	foo = str(foo)
	for a in xrange(0, (len(foo)/2)+1):
		if foo[a] == foo[-(a+1)]:
			a += 1
			continue
		else:
			return False
	return True

lista = []
for a in xrange(100, 1000):
	for b in xrange(100, 1000):
		number = a*b
		if checkpalindrome(number):
			lista.append(number)
lista.sort()
print lista[-1]
			
