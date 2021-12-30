import sys
import numpy as np
import cv2


src = cv2.imread(r'C:\coding\python\opencv\ch06\lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 에지 : 영상에서 픽셀의 밝기 값이 급격하게 변하는 부분으로 객체와 객체의 경계
# 영상을 (x,y) 변수의 함수로 간주했을 때, 이 함수의 1차 미분 값이 크게 나타나는 부분을 검출

# 소벨 필터를 이용한 미분 함수
dx = cv2.Sobel(src, -1, 1, 0, delta=128)
dy = cv2.Sobel(src, -1, 0, 1, delta=128)

cv2.imshow('src', src)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.waitKey()

cv2.destroyAllWindows()
