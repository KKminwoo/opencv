import sys
import numpy as np
import cv2

src = cv2.imread(r'C:\coding\python\opencv\ch04\rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 언샤프 마스크 필터
# 날카롭지 않은(unsharp) 영상, 부드러운 영상을 이용하여 날카로운 영상을 생성
blr = cv2.GaussianBlur(src, (0, 0), 2)
dst = np.clip(2.0*src - blr, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
