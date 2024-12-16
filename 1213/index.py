
import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

path = "C:\\Windows\\Fonts\\Hancom Gothic Bold.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)
# # 이미지 읽기
# image = cv2.imread("./1213/test_image.jpg")

# # opencv BGR -> RGB
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# ========================================================
'''
# cv2.imshow('title', image_rgb)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.imshow(image_rgb)
plt.axis('off')
plt.show()
'''
'''
# 노이즈 제거거
# ========================================================

plt.figure(figsize=(10, 8))
# 원본
plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title("원본")
plt.axis('off')

# 평균블러
blurred = cv2.blur(image_rgb, (5, 5))
plt.title("평균블러")
plt.subplot(2, 2, 2)
plt.imshow(blurred)
plt.axis('off')


# ========================================================

# 가우시안 블러링
gaussian_blurred = cv2.GaussianBlur(image_rgb, (5, 5), 0)

plt.subplot(2, 2, 3)
plt.imshow(gaussian_blurred)
plt.title("가우시안 블러")
plt.axis('off')


# ========================================================

# 미디언 블러링
median_blur = cv2.medianBlur(image_rgb, 5)

plt.subplot(2, 2, 4)
plt.imshow(median_blur)
plt.title("미디안 블러")
plt.axis('off')
'''
# ========================================================
'''
# 샤프닝 커널
plt.figure(figsize=(10, 10))
# 원본
plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title("원본")
plt.axis('off')
# 중심값을 크게 설정하여 엣지를 강조
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]
                   ])

# 필터 적용
sharped = cv2.filter2D(image_rgb, -1, kernel)

plt.subplot(2, 2, 2)
plt.imshow(sharped)
plt.title("엣지 강조")
plt.axis('off')
'''
# ========================================================
'''
img = cv2.imread("./1213/test_image.jpg", cv2.IMREAD_GRAYSCALE)
plt.figure(figsize=(10, 10))
# 원본
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("원본")
plt.axis('off')

# 엣지 검출

# sobel
# x 방향 미분
# 64 opencv에 정의된 정수 64비트 float 예) 8U = 8비트 0~255까지
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
# y 방향 미분
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

sobel_combined = cv2.magnitude(sobel_x, sobel_y)
plt.subplot(2, 2, 2)
plt.imshow(sobel_combined, cmap='gray')
plt.title("sobel")
plt.axis('off')


# laplacian
laplacian = cv2.Laplacian(img, cv2.CV_64F)

plt.subplot(2, 2, 3)
plt.imshow(laplacian, cmap='gray')
plt.title("llaplacian")
plt.axis('off')


# canny
edges = cv2.Canny(img, 100, 200)  # 최소값, 최대값

plt.subplot(2, 2, 4)
plt.imshow(edges, cmap='gray')
plt.title("canny")
plt.axis('off')
plt.show()
'''
# ========================================================
'''
# 원본
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.subplot(2, 2, 1)
plt.imshow(gray, cmap='gray')
plt.title("원본")
plt.axis('off')
# 컨투어
# 이진화 처리
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 컨투어 감지
contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 컨투어 원본에 그리기
results_img = image.copy()
cv2.drawContours(results_img, contours, -1, (0, 255, 0), 2)
plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(results_img, cv2.COLOR_BGR2RGB))
plt.title("컨투어 그리기")
plt.axis('off')
plt.show()
'''
# ========================================================

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# results_img = image.copy()

# for contour in contours:
# 면적계산
# print("면적 : ", cv2.contourArea(contour))

# 중심점 계산
# M = cv2.moments(contour)
# if M['m00'] != 0:  # 중심점 계산 (m00 = 면적)
#     cx = int(M['m10'] / M['m00'])  # x중심
#     cy = int(M['m01'] / M['m00'])  # y중심

#     # 중심점 표시
#     cv2.circle(results_img, (cx, cy), 5, (0, 0, 0), -1)
# else:
#     print("컨투어 면적이 : 0")
# 둘레 계산
# print("둘레 : ", cv2.arcLength(contour, True))  # 폐곡선 여부

# cv2.drawContours(results_img, [contour], -1, (0, 255, 0), 2)
# pass
# plt.imshow(cv2.cvtColor(results_img, cv2.COLOR_BGR2RGB))
# plt.axis('off')
# plt.show()
# ========================================================
'''
# 웹캠 연결
cap = cv2.VideoCapture(0)

# codec = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('./1213/output.avi', codec, 20.0, (640, 480))
plt.ion()  # 인터렉티드 모드: 코드를 실행하면서 창을 표시시
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:  # TRUE FALSE 값 판별
        break

    # out.write(frame)
    # cv2.imshow("video", frame)
    # 원본
    original = frame.copy()

    # 가우시안 블러
    gaussian = cv2.GaussianBlur(frame, (7, 7), 0)

    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title("원본")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB))
    plt.title("가우시안 블러")
    plt.axis('off')

    plt.pause(0.001)  # 1밀리초동안
    plt.clf()  # 현재 플롯창에 띄어진 것을 초기화

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
plt.close()
'''
# ========================================================

# 실습.손 윤곽선을 감지하고 필터를 추가
# 웹캠 연결
cap = cv2.VideoCapture(0)
plt.ion()
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
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title("원본")
    plt.axis('off')

    # 윤곽선 그리기기
    plt.subplot(2, 2, 2)
    plt.imshow(cv2.cvtColor(contour_frame, cv2.COLOR_BGR2RGB))
    plt.title("컨투어")
    plt.axis('off')

    # 샤프팅 필터터qqqq
    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(sharped, cv2.COLOR_BGR2RGB))
    plt.title("샤프닝")
    plt.axis('off')

    plt.pause(0.001)
    plt.clf()

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
plt.ioff()
