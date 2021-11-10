import numpy as np
import cv2

# img는 흰색으로 채워진 사이즈의 이미지
img = np.full((400, 400, 3), 255, np.uint8)

# 선 그리기. 그림을 그릴 영상, 시작점, 끝점, 선 색상 밝기, 선 두께(기본값 1)
cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5) # 두꺼운 선
cv2.line(img, (50, 60), (150, 160), (0, 0, 128))

# 사각형 그리기.
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1) # 음수로 설정할 경우 내부를 채움

# 원 그리기
cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

# 다각형 그리미. 꼭짓지점을 ndarray 형태로 표현
pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]]) # 4개의 점을 2차원 행렬로 표시
cv2.polylines(img, [pts], True, (255, 0, 255), 2) # pts를 입력할 시 리스트 형태 []로 표현

# 문자열 출력
text = 'Hello? OpenCV ' + cv2.__version__
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
            (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()

