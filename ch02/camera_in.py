import sys
import cv2


# 카메라 여는 class 생성
video = 'C:\coding\python\opencv\ch02\video1.mp4'
cap = cv2.VideoCapture(0)

# 정상적으로 카메라가 열었는지 확인
if not cap.isOpened(): 
    print("Camera open failed!")
    sys.exit()

# 카메라 프레임 크기 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 카메라 프레임 크기 조정
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)

# 카메라 프레임 처리
while True:
    # 두 개의 변수 받아오는 순서 확인하기
    ret, frame = cap.read()

    # retry 인자 확인
    if not ret:
        break

    # 윤곽선만 딴 영상
    edge = cv2.Canny(frame,50,150)
    # 반전
    inversed = ~frame 

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)
    cv2.imshow('edge', edge)

    if cv2.waitKey(10) == 27: # esc 눌렀을 때 빠져나옴
        break

cap.release()
cv2.destroyAllWindows()
