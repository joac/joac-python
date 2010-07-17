#!/usr/lib/env python
# -*- coding: utf-8 -*-

def triangleMaxPath(triangle):
    for a in xrange(1, len(triangle)):
        rowWidth = len(triangle[a])
        for b in xrange(0, rowWidth):
         
            previousA = triangle[a-1][b-1]
            if b<(rowWidth-1):
                previousB = triangle[a-1][b]
                if b:     
                    triangle[a][b] += max([previousA, previousB])   
                else:
                    triangle[a][b] += previousB
            else:
                triangle[a][b] += previousA
    return max(triangle[-1])

file=open('triangle.txt')
contents = file.read().splitlines()
file.close()
contents = [line.split() for line in contents]
triangle = []
for line in contents:
    triangle.append([int(a) for a in line])

print triangleMaxPath(triangle)

