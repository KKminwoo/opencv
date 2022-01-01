import sys
import numpy as np
import cv2


src = cv2.imread(r'C:\coding\python\opencv\ch06\building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 캐니 에지 검출
# 1. 가우시안 필터링 : 잡음 제거 목적
# 2. 그래디언트 계산 : 주로 소벨 마스크 사용
# 3. 비최대 억제 : 하나의 에지가 여러 개의 픽셀로 표현되는 현상을 없애기 위해 그래디언트 크기가 로컬 최대인 엑셀만을 에지 픽셀로 설정
# 4. 히스테리시스 에지 트래킹 : 두 개의 임계값을 사용하여 강한 에지를 최종 에지로 선청
dst = cv2.Canny(src, 50, 150)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
