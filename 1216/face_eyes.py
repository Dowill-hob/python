
import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

path = "C:\\Windows\\Fonts\\Hancom Gothic Bold.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)
# ===================================================================================
''' HSV
img = cv2.imread("./1216/test_image.jpg")

# BGR -> HSV 변환
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 색상범위 설정 (빨강색)
lower = np.array([0, 120, 70])
upper = np.array([10, 255, 255])

# 마스크 생성
mask = cv2.inRange(hsv_image, lower, upper)

# 원본이미지에 마스크 적용
result = cv2.bitwise_and(img, img, mask=mask)

plt.subplot(1, 3, 1)
plt.title('Original')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("mask")
plt.imshow(mask, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("result")
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
'''
# ===================================================================================
'''
# 실시간 피부색 검출
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 크기변경
    frame = cv2.resize(frame, (640, 480))

    # HSV로 변경
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 피부색 범위(HSV)
    lower = np.array([0, 20, 70])
    upper = np.array([20, 255, 255])

    # 마스크 생성
    mask = cv2.inRange(hsv, lower, upper)

    # 노이즈제거(모폴로지 연산)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # 컨투어 찾기
    contours, _ = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 윤곽선 그리기
    for con in contours:
        area = cv2.contourArea(con)

        cv2.drawContours(frame, [con], -1, (0, 255, 0), 3)

    cv2.imshow("피부색", frame)
    cv2.imshow("마스크", mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''
# ===================================================================================
'''
# 얼굴인식
# haar cascade 불러오기
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 그레이 스케일로 변환
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴탐지
    faces = face_cascade.detectMultiScale(
        gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 탐지된 얼굴에 사각형 그리기
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('face', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''
# ===================================================================================

# 얼굴 눈 인식
# 얼굴
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# 눈
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # 눈 탐지
        eyes = eye_cascade.detectMultiScale(
            gray_frame, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15))

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0, 255, 0))
    cv2.imshow('eyes', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
