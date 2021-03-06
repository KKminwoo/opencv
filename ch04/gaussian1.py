import sys
import numpy as np
import cv2


src = cv2.imread(r'C:\coding\python\opencv\ch04\rose.bmp', cv2.IMREAD_GRAYSCALE)

# 가우시안 함수
# 가까이 있는 픽셀은 큰 가중치를, 멀리 있는 픽셀은 작은 가중치를 사용하여 평균 계산
dst = cv2.GaussianBlur(src, (0, 0), 3)
dst2 = cv2.blur(src, (7, 7))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
