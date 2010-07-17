file = open('names.txt')

contents = file.read()
file.close()
contents = contents.strip('"')
contents = contents.split('","')

contents.sort()

total = 0

for word in contents:
    a = 0
    for char in word:
        a+=(ord(char)-64)
    b = contents.index(word)+1
    print b, word
    total += (a*b)

print total

