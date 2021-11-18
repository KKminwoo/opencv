import numpy as np
import cv2


def on_level_change(pos):
    value = pos * 16
    # 포화 연산 : 255보다 값이 커질 경우 계속 255 값으로 나타내는 것 
    value = np.clip(value,0,255)
    # if value >= 255:
    #     value = 255

    img[:] = value
    cv2.imshow('image', img)

# grey scale 영상 출력
img = np.zeros((480, 640), np.uint8)

cv2.namedWindow('image')

# 반드시 영상을 출력한 후 실행 0~16까지의 단계 실행
cv2.createTrackbar('level', 'image', 0, 16, on_level_change)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
