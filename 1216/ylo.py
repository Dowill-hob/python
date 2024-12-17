'''
# YOLO 테스트
from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt') # YOLO모델 V8, n: nano버전

image = cv2.imread('./1216/test.jpg')

# 객체 탐지
results = model.predict(source=image, save=False,
                        save_txt=False, conf=0.5)  # conf 신뢰도

# 결과 시각화
frame = results[0].plot()  # plot() : 탐지된 객체를 시각화한 이미지를 반환

cv2.imshow('YOLO', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# ============================================================================
'''
# OCR

# Tesseract 경로 설정
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# 이미지 가져오기
image = cv2.imread('./1216/receiot.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray_image, lang='kor')
print("추출된 이미지", text)
'''
# ============================================================================
'''
# OCR 발전
# Tesseract 경로 설정
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# 이미지 가져오기
image = cv2.imread('./1216/car_number.png')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 관심영역 설정
roi = gray_image[250:429, 119:685]

binary_img = cv2.adaptiveThreshold(
    roi, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 5)
# cv2.adaptiveThreshol() : 조명에 대응이 쉽다

text = pytesseract.image_to_string(binary_img, lang='kor')
# cv2.imshow("check", binary_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
print("추출된 이미지", text)
'''
# ============================================================================


import matplotlib.pyplot as plt
import pytesseract
import numpy as np
import cv2
img = cv2.imread("./1216/fruite.png")
# BGR -> HSV 변환
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 색상범위 설정 (초록색)
lower = np.array([40, 50, 50])
upper = np.array([80, 255, 255])
# 마스크 생성
green_mask = cv2.inRange(hsv_image, lower, upper)
# 원본이미지에 마스크 적용
green_region = cv2.bitwise_and(img, img, mask=green_mask)

# 윤곽선 검출
contours, _ = cv2.findContours(
    green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

count = 0

for con in contours:
    if cv2.contourArea(con) > 50:  # 작은 노이즈 제거
        x, y, w, h = cv2.boundingRect(con)  # 객체를 감싸는 가장 작은 축에 정렬된 사각형
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        count += 1
cv2.imshow('Original Image', img)
print(f"검출된 초록색 물체 개수 : {count} 개")
cv2.waitKey(0)
cv2.destroyAllWindows()
