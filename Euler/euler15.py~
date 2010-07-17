def PascalTriangle(rows):
    triangle = []
    for a in xrange(0, rows):
        rowWidth = a+1
        line = []
        for b in xrange(0, rowWidth):
            if a and b and (b<(rowWidth-1)):
                previousB = triangle[a-1][b]
                previousA = triangle[a-1][b-1]
                line.append(previousA+previousB)
            else:
                line.append(1)
        #else: line.append(1)
        triangle.append(line)    
    return triangle

a = PascalTriangle(41)
a = a[-1]
print a
print 'resultado: %d' % max(a)
print 'largo: %d' %len(a)


    
    
