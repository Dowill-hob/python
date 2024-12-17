
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

path = "C:\\Windows\\Fonts\\Hancom Gothic Bold.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)
# ---------------------------------------------------------------
# # 히스토그램
# data = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 5, 6]
# # bins = 5 = [1,2][2,3][3,4][4,5][5,6]

# plt.hist(data, bins=5, color="green", histtype="stepfilled")

# plt.title("히스토그램")
# plt.xlabel("값")
# plt.ylabel("빈도수")
# plt.grid()
# plt.show()
# ---------------------------------------------------------------
# 여러개 data
# data1 = [1, 2, 2, 3, 3, 3, 4]
# data2 = [2, 3, 3, 4, 4, 5, 6]

# plt.hist([data1, data2], bins=5, color=["#ff2233", "#22ff33"],
#          alpha=0.8, label=["data1", "data2"])
# plt.legend()
# plt.title("히스토그램 여러개")
# plt.xlabel("값")
# plt.ylabel("빈도수")
# plt.grid()
# plt.show()
# # ---------------------------------------------------------------
# 산점도
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]
# sizes = [20, 50, 80, 100, 200]
# colors = [10, 20, 30, 40, 50]
# plt.scatter(x, y, s=sizes, c=colors, cmap="viridis")
# plt.colorbar(label="color bar")
# plt.grid()
# plt.show()
# ---------------------------------------------------------------
# 산점도 그리기
# n = 50
# x = np.random.rand(n)  # 0과 1 사이 난수
# y = np.random.rand(n)

# area = (30 * np.random.rand(n)) ** 2  # 0과 30사이 난수 생성 후 제곱하여 크기 생성
# colors = np.random.rand(n)
# plt.scatter(x, y, s=area, c=colors, cmap="Spectral", alpha=0.8)
# plt.grid()
# plt.show()
# ---------------------------------------------------------------
# 파이차트 그리기
# 강조 파이차트
# sizes = [15, 30, 45, 10]
# labels = ['사과', '수박', '바나나', '딸기']
# explode = [0, 0, 0.1, 0]

# plt.pie(sizes, labels=labels, explode=explode,
#         autopct="%1.1f%%", shadow=True, startangle=140)
# plt.show()
# 색상 꾸미기
# sizes = [10, 20, 30, 40]
# labels = ['A', 'B', 'C', 'D']
# colors = ["gold", 'lightblue', 'lightgreen', 'pink']

# plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors,
#         textprops={"fontsize": 15, "color": "darkblue", "weight": "bold"}, wedgeprops={"edgecolor": "black"})

# plt.show()
# ---------------------------------------------------------------
# 도넛
# sizes = [40, 30, 20, 10]
# labels = ['X', 'Y', 'Z', 'W']

# plt.pie(sizes, labels=labels, wedgeprops={"width": 0.4})

# plt.show()
# ---------------------------------------------------------------
# 실습1. 그래프 그리기

# months = ['Jan', 'Feb', 'Mar', 'Apr', "May", "Jun",
#           "Jul", 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# sales_2019 = [100, 120, 140, 110, 130, 150, 160, 170, 180, 200, 190, 210]
# sales_2020 = [90, 110, 130, 120, 140, 160, 170, 160, 150, 180, 200, 190]

# plt.plot(months, sales_2019, color="b", label="2019")
# plt.plot(months, sales_2020, color="orange", label="2020")
# plt.title("Monthly Sales Comparsion (2019-2020)")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.legend()
# plt.show()
# ---------------------------------------------------------------
# 실습2. 그래프 그리기
plt.figure(figsize=(8, 10))  # 창 크기
categories = ['Category1', 'Category2', 'Category3', 'Category4', 'Category5']
data = [20, 35, 15, 27, 45]
plt.bar(categories, data)
plt.title("Bar Chart")  # 제목
plt.xlabel("Categories")  # x축
plt.ylabel("Values")    # y축
plt.xticks(rotation=45)  # x축 레이블 회전
plt.ylim([0, 50])  # y축 limit
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
# ---------------------------------------------------------------
# 실습3. 그래프 그리기
sizes = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']
explode = [0, 0.1, 0, 0.1]
colors = ['#dc143c', '#ffff00', '#008000', '#800080']
plt.pie(sizes, labels=labels, explode=explode, colors=colors,
        wedgeprops={"width": 0.8, "edgecolor": "black"}, autopct="%1.1f%%", textprops={"fontsize": 15, "color": "black", "weight": "bold"})
plt.show()
# ---------------------------------------------------------------
