import sys
import numpy as np
import cv2


src = cv2.imread(r'C:\coding\python\opencv\ch07\rice.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# Otsu 이진화 방법(최적화 알고리즘) -> 전경&배경의 픽셀 분포가 비슷할 때 사용
# 임의의 임계값에 의해 나눠지는 두 픽셀 분포 그룹의 분산이 최소가 되는 임계값을 선택
th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print("otsu's threshold:", th)  # 131

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
