import cv2
import numpy as np
"""
# source 폴더에서 이미지 불러오기
- IMREAD_UNCHANGED(컬러읽고 투명부분도 읽어옴)
- IMREAD_COLOR(컬러읽고 투명부분은 무시)
- IMREAD_GRAYSCALE(회색으로 읽어옴)
"""
# ===============================================================================
'''
# image = cv2.imread('./1212/owl.png')
image = cv2.imread('./1212/owl.png', cv2.IMREAD_GRAYSCALE)
image_color = cv2.imread('./1212/owl.png')

print(image.shape)
print(image_color.shape)


cv2.imshow("Gray Image", image)
cv2.imshow("Color Image", image_color)

# cv2.imwrite("./1212/output-owl.jpg", image)

cv2.waitKey(2000)  # 창만 닫히고 윈도우는 남아있을수 있음
cv2.destroyAllWindows()  # 윈도우에 남아있는 메모리까지 닫음 보통 둘을 같이씀


# key = cv2.waitKey(0)  # 딜레이 1000 = 1초
# if key == ord('q'): # q로 창을 닫을때 만 처리 다른키는 아무것도 출력 X
#     print(chr(key))
'''
# ========================================================================

'''
image_color = cv2.imread("./1212/owl.png")
# gray = cv2.cvtColor(image_color, cv2.COLOR_RGB2GRAY)
# hsv = cv2.cvtColor(image_color, cv2.COLOR_BGR2HSV)
# resized = cv2.resize(image_color, (400,300))

roi = image_color[100:500, 200:400].copy()
# scale = 0.5
# resized = cv2.resize(image_color, None, fx=scale, fy=scale)
cv2.imshow("Color image", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
# ========================================================================
'''
# x값 y값 찾기기
def mouse_click(e, x, y, flag, param):
    if e == cv2.EVENT_LBUTTONDOWN:
        print(f"마우스 위치: x = {x}, y = {y}")


image_color = cv2.imread("./1212/owl.png")

cv2.imshow("image", image_color)
# 마우스 콜백함수
cv2.setMouseCallback("image", mouse_click)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
# ========================================================================
'''
# roi 만 표시
# 글로벌 변수
start = None
end = None


def mouse_select(e, x, y, flag, param):
    global start, end
    if e == cv2.EVENT_LBUTTONDOWN:  # 클릭을 누르는 상태
        start = (x, y)
    elif e == cv2.EVENT_LBUTTONUP:  # 클릭을 뗀 상태
        end = (x, y) 
        # 영역 표시
        roi = image_color[start[1]:end[1], start[0]:end[0]]
        cv2.imshow("select", roi)


image_color = cv2.imread("./1212/owl.png")

cv2.imshow("image", image_color)

# 마우스 콜백함수
cv2.setMouseCallback("image", mouse_select)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
# ========================================================================
'''
# 회전 및 이동
image = cv2.imread("./1212/owl.png")

# 중심 좌표
(h, w) = image.shape[:2]
center = (w//2, h//2)

# 회전
# matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
# rotated = cv2.warpAffine(image, matrix, (w, h))

# 이동
matrix = np.float32([[1, 0, 100], [0, 1, 50]])
move = cv2.warpAffine(image, matrix, (w, h))

cv2.imshow("image", move)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
# ========================================================================
'''
# 실습 1-1
image = cv2.imread("./1212/owl.png")
print(image.shape)

# # 실습 1-2
image = cv2.imread("./1212/owl.png")
black_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("black-image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # 실습 1-3
image = cv2.imread("./1212/owl.png")
scale = 0.5
resize = cv2.resize(image, None, fx=scale, fy=scale)
cv2.imshow('image', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 실습 1-4
image = cv2.imread("./1212/owl.png")
(h, w) = image.shape[:2] 
center = (w//2, h//2)

matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(image, matrix, (w, h))

cv2.imshow('image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
