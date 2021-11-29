import sys
import numpy as np
import cv2


src = cv2.imread('C:\coding\python\opencv\ch03\candies.png')
#src = cv2.imread('candies2.png')

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# rgb 기준으로 녹색 영역 추출하기
dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))
# hsv 기준으로 녹색 영역 추출하기
dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
