import sys
import numpy as np
import cv2


src = cv2.imread(r'C:\coding\python\opencv\ch05\tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# 영상의 중앙 기준 회전
cp = (src.shape[1] / 2, src.shape[0] / 2)
rot = cv2.getRotationMatrix2D(cp, 20, 0.5)

dst = cv2.warpAffine(src, rot, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
