# OpenCV를 활용한 컴퓨터비전과 딥러닝
- study with [Fast campus]
## 1. Install
### OpenCV main modules
[GitHub - opencv/opencv: Open Source Computer Vision Library](https://github.com/opencv/opencv)

### Python 설치하기

[Python Release Python 3.7.7](https://www.python.org/downloads/release/python-377/)

### OpenCV 설치

```cpp
pip install opencv-python
```

- 커맨드 창에서 확인

```cpp
python

import cv2
```
---

## 2. Preview
### 영상

: 픽셀이 바둑판 모양의 격자에 나열되어 있는 2차원 행렬 형태
→ 픽셀 : 영상의 기본 단위, 화소

### greyscale 영상

 : 밝기 정보만으로 0~256단계로 구성된 영상
1바이트 프로그래밍 언어 사용
C/C++ → unsigned char
Python → numpy.uint8
![Untitled](https://user-images.githubusercontent.com/47807421/136975135-0ca699a6-a4ab-4344-a397-328296da6dfe.png)

### truecolor 영상

 :  R,G,B 색 성분을 256단계로 표현 → 256의 3승 16백만가지

3바이트 프로그래밍 언어 사용

C/C++ → 구조체, 클래스
Python → 튜플, numpy.ndarray

![Untitled (2)](https://user-images.githubusercontent.com/47807421/136975278-466d96fd-a89c-432a-9c02-0bce7b9c464d.png)

### 영상에서 주로 사용되는 좌표계
![Untitled (1)](https://user-images.githubusercontent.com/47807421/136975432-44c457b0-1e21-4610-9367-efc806f95c37.png)

### 영상 데이터 크기 분석

- 그레이스케일 영상 : 가로 x 세로(Byties)
- 트루컬러 영상 : 가로 x 세로 x 3(Bytes) → RGB로 3차원
⇒ 연산량에 따른 시간을 줄이는 것이 중요하다!
