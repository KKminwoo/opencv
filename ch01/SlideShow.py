import sys
import glob
import cv2


# 경로상의 이미지 파일을 모두 img_files 리스트에 추가
img_files = glob.glob('C:\coding\python\opencv\ch01\images\\*.jpg')

if not img_files:
    print("There are no jpg files in 'images' folder")
    sys.exit()

# 전체 화면으로 'image' 창 생성
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# 이미지 파일의 갯수 파악
cnt = len(img_files)
idx = 0

# 무한 루프
while True:
    # 첫 번째 이미지 불러오기
    img = cv2.imread(img_files[idx])

    if img is None:
        print('Image load failed!')
        break

    cv2.imshow('image', img)
    
    # 키보드의 아무키나 누를 경우 종료
    if cv2.waitKey(1000) >= 0:
        break

    idx += 1
    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()
