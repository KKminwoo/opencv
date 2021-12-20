import sys
import numpy as np
import cv2

src = cv2.imread(r'C:\coding\python\opencv\ch04\lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# 양방향 필터
# 에지 보전 잡음 제거 필터 중 하나
# 평균값 필터, 가우시안 필터는 에지 부근에서 픽셀 값을 평탄하게 만드는 단점이 있음
# 기준 픽셀과 이웃 픽셀과의 거리, 그리고 픽셀 값의 차이를 함께 고려하여 블러링 정도를 조절
dst = cv2.bilateralFilter(src, -1, 10, 5)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
