import matplotlib.pyplot as plt
import cv2

# 컬러 영상 출력
img_file = 'C:\coding\python\opencv\ch01\cat.bmp'
imgBGR = cv2.imread(img_file)

# cv2.imread() 함수로 불러온 이미지 색상 정보는 BGR 순서이므로 이를 RGB 순서로 변경해야 함
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

# 눈금 꺼버리기 
plt.axis('off')

# 반드시 RGB 순으로 실행시켜야 함
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력
# plt.imshow() 함수에서 컬러맵을 cmap='grey'로 지정
imgGray = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()
