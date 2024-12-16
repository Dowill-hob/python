
import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager


# 실습.손 윤곽선을 감지하고 필터를 추가
# 웹캠 연결
cap = cv2.VideoCapture(0)
plt.ion()
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:  # TRUE FALSE 값 판별
        break

    # 원본
    original = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 이진화 처리
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # 컨투어 처리
    contours, _ = cv2.findContours(
        binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 컨투어 그리기
    contour_frame = frame.copy()
    cv2.drawContours(contour_frame, contours, -1, (0, 255, 0), 2)

    # 샤프닝 필터
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]
                       ])
    sharped = cv2.filter2D(contour_frame, -1, kernel)

    # 원본
    # plt.subplot(2, 2, 1)
    axes[0, 0].imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    axes[0, 0].set_title("원본")
    axes[0, 0].axis('off')

    # 윤곽선 그리기기
    # plt.subplot(2, 2, 2)
    axes[0, 1].imshow(cv2.cvtColor(contour_frame, cv2.COLOR_BGR2RGB))
    axes[0, 1].set_title("컨투어")
    axes[0, 1].axis('off')

    # 샤프팅 필터터qqqq
    # plt.subplot(2, 2, 3)
    axes[1, 0].imshow(cv2.cvtColor(sharped, cv2.COLOR_BGR2RGB))
    axes[1, 0].set_title("샤프닝")
    axes[1, 0].axis('off')

    plt.pause(0.001)
    # plt.clf()

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
plt.ioff()  # 인터렉티브 모드 종료
