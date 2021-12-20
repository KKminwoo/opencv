import sys
import numpy as np
import cv2

src = cv2.imread('noise.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 미디언 필터
# 주변 픽셀들의 값들을 정렬하여 그 중앙값으로 픽셀 값을 대체
dst = cv2.medianBlur(src, 3)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
