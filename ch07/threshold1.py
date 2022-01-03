import sys
import numpy as np
import cv2

# 영상의 이진화 : 영상의 픽셀 값을 0 또는 255(1)로 만드는 연산

src = cv2.imread(r'C:\coding\python\opencv\ch07\cells.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

_, dst1 = cv2.threshold(src, 150, 255, cv2.THRESH_BINARY)
_, dst2 = cv2.threshold(src, 210, 255, cv2.THRESH_BINARY)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
