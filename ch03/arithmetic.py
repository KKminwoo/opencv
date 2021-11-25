import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


src1 = cv2.imread('C:\coding\python\opencv\ch03\lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('C:\coding\python\opencv\ch03\square.bmp', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

# 덧셈 연산
dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U)
# 가중치 합
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
# 뺄셈 연산
dst3 = cv2.subtract(src1, src2)
# 차이 연산
dst4 = cv2.absdiff(src1, src2)

plt.subplot(231), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
plt.subplot(232), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
plt.subplot(233), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('add')
plt.subplot(234), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('addWeighted')
plt.subplot(235), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('subtract')
plt.subplot(236), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('absdiff')
plt.show()
