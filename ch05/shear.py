import sys
import numpy as np
import cv2


src = cv2.imread(r'C:\coding\python\opencv\ch05\tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# 전단 변환 : x축과 y축 방향에 대해 따로 정의
aff = np.array([[1, 0.5, 0],
                [0, 1, 0]], dtype=np.float32)

h, w = src.shape[:2]
dst = cv2.warpAffine(src, aff, (w + int(h * 0.5), h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
