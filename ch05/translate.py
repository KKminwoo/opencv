import sys
import numpy as np
import cv2


src = cv2.imread(r'C:\coding\python\opencv\ch05\tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# 이동 변환 : x,y축 방향으로 이동 변위를 2*3 어파인 변환 행렬로 지정
aff = np.array([[1, 0, 200],
                [0, 1, 100]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
