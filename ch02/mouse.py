import sys
import numpy as np
import cv2


oldx = oldy = -1

def on_mouse(event, x, y, flags, param):
    global oldx, oldy

    # 클릭한 좌표값 출력
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))
    
    # 클릭하고 땐 좌쵸값 출력
    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))

    # 클릭했을때 선 그리기
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
            cv2.imshow('image', img)
            oldx, oldy = x, y

# 모든 픽셀이 255 rgb -> 흰색으로 나타남
img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('image')

# 윈도우를 띄운 이후에 setMouseCallbaack 함수 실행시켜야 함
cv2.setMouseCallback('image', on_mouse, img)

cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()
