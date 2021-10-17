import cv2
import sys

print("First Code Hello, openCV", cv2.__version__)

# 이미지 파일 불러오기
img_file = 'C:\coding\python\opencv\ch01\cat.bmp'
img = cv2.imread(img_file,cv2.IMREAD_GRAYSCALE)

# 예외처리 
if img is None:
    print('Image load failed!')
    sys.exit()

# 이미지 저장
# cv2.imwrite('cat_gray.png',img)

# 이미지를 받아오는 창 생성 -> default 값으로 창 사이즈에 맞는 크기로 이미지 설정
cv2.namedWindow('image')

# 이미지를 보여줌 
cv2.imshow('image',img)

while True:
    # 영상이 보여줄 수 있게끔 작업 -> 이미지를 보여주기 위해서는 반드시 위 함수가 필요
    # 아스키 코드 27 = ESC
    if cv2.waitKey()==27:
        break

# 모든 창을 닫음
cv2.destroyAllWindows()