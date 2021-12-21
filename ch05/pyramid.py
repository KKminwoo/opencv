import sys
import numpy as np
import cv2


src = cv2.imread(r'C:\coding\python\opencv\ch05\cat.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()


rc = (250, 120, 200, 200)  # rectangle tuple

# 원본 영상에 그리기
cpy = src.copy()
cv2.rectangle(cpy, rc, (0, 0, 255), 2)
cv2.imshow('src', cpy)
cv2.waitKey()

# 피라미드 영상에 그리기
for i in range(1, 4):
    # 이미지 피라미드 다운샘플링
    # 하나의 영상에 대해 다양한 해상도의 영상 세트를 구성한 것
    # 보통 가우시안 블러링 & 다운샘플링 형태로 축소하여 구성
    src = cv2.pyrDown(src)
    cpy = src.copy()
    cv2.rectangle(cpy, rc, (0, 0, 255), 2, shift=i)
    cv2.imshow('src', cpy)
    cv2.waitKey()
    cv2.destroyWindow('src')

cv2.destroyAllWindows()
