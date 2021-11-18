import sys
import time
import numpy as np
import cv2

# 15MB 용량의 사진
img = cv2.imread('hongkong.jpg')

# 연산 시간을 측정
tm = cv2.TickMeter()

tm.reset()
tm.start()
t1 = time.time()

# edge 검출해내는 함수
edge = cv2.Canny(img, 50, 150)

tm.stop()
print('time:', (time.time() - t1) * 1000)
print('Elapsed time: {}ms.'.format(tm.getTimeMilli()))

