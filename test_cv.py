# coding: utf-8
import cv2

cv2.namedWindow('Original')
cv2.namedWindow('Test')

a = cv2.imread('test_blobs.png')

gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

ret, b = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)

cv2.imshow('Test', b)

contornos, jerarquia = cv2.findContours(b, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contornos:
    center, radius = cv2.minEnclosingCircle(cnt)
    center = tuple(map(int, center))
    radius = int(radius)
    cv2.circle(a, center, radius, (255, 0, 0), 5)

cv2.imshow('Original', a)

while True:
    if cv2.waitKey(1) == 27:
        break

