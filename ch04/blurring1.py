import sys
import numpy as np
import cv2


src = cv2.imread(r'C:\coding\python\opencv\ch04\rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

#kernel = np.ones((3, 3), dtype=np.float64) / 9.
#dst = cv2.filter2D(src, -1, kernel)

# 평균 값 필터링 함수
# -> 영상의 특정 좌표 값을 주변 픽셀 값들의 산술 평균으로 설정
# -> 픽셀들 간의 그레이스케일 값 변화가 줄어들어 날카로운 에지가 무뎌지고, 영상의 잡음의 영향이 사라짐
dst = cv2.blur(src, (4, 4))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
