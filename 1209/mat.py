import matplotlib.pyplot as plt
from matplotlib import font_manager

# font_list = font_manager.findSystemFonts(fontpaths=None, fontext="ttf") # 폰트 경로찾기
# print(font_list)

path = "C:\\Windows\\Fonts\\Hancom Gothic Bold.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)
# ---------------------------------------------------------------------------
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# # plt.plot(x, y, color="#ff2244", linestyle='--', linewidth=3, label='샘플그래프')
# # plt.title('Matplotlib 그래프 그리기', fontsize=20, pad=20, backgroundcolor="#2233ff", color="#66ff33")
# plt.plot(x, y, marker="d", markersize=20,
#          markerfacecolor="yellow", markeredgecolor="green")

# font = {
#     "size": 20,
#     "color": "white",
#     "backgroundcolor": "black",
#     "weight": "bold"
# }
# plt.legend(title="범례명", fontsize=13, loc="lower center")
# plt.grid(True, axis="x", linestyle="--", color="#000000", alpha=0.5)
# plt.title('Matplotlib 그래프 그리기', pad=10, fontdict=font)
# plt.xlabel("x 축", fontdict=font, labelpad=20)
# plt.ylabel("y 축", fontdict=font)

# # plt.xlim([0, 15])
# # plt.ylim([0, 15])
# # plt.axis("equal")
# # plt.axis("scaled")
# # plt.axis("auto")
# # plt.axis([0, 10, 0, 15])
# plt.axis("tight")
# plt.show()
# -------------------------------
# 그래프 선 여러개
# x = [1, 2, 3, 4]
# y1 = [1, 2, 3, 4]
# y2 = [2, 4, 6, 8]
# y3 = [3, 6, 9, 12]
# y4 = [4, 8, 12, 16]
# font = {
#     "size": 15,
#     "color": "red",
#     "style": "italic",
#     "weight": "bold"
# }
# plt.plot(x, y1, label="y=x", color="red", marker='o')
# plt.plot(x, y2, label="y=2x", color="orange", marker='<')
# plt.plot(x, y3, label="y=3x", color="black", marker='>')
# plt.plot(x, y4, label="y=4x", color="#3344ff", marker='*')

# plt.grid()

# plt.legend(loc="upper center", title="4개연습", ncol=4)
# plt.title("그래프 그리기 연습", fontdict=font)
# plt.xlabel("x값")
# plt.ylabel("y값")

# plt.show()
# ---------------------------------
# 그래프 자체가 여러개
# x = [1, 2, 3, 4]
# y1 = [1, 2, 3, 4]
# y2 = [2, 4, 6, 8]
# y3 = [3, 6, 9, 12]
# y4 = [4, 8, 12, 16]
# plt.subplot(2, 2, 1)
# plt.plot(x, y1)
# plt.title("x=y")

# plt.subplot(2, 2, 2)
# plt.plot(x, y2)
# plt.title("x=2y")

# plt.subplot(2, 2, 3)
# plt.plot(x, y3)
# plt.title("x=3y")

# plt.subplot(2, 2, 4)
# plt.plot(x, y4)
# plt.title("x=4y")

# plt.suptitle("그래프 그리기 연습")
# plt.tight_layout()

# plt.show()
# -----------------------------------------------------------
# 막대 그래프
# font = {
#     "size": 15,
#     "color": "red",
#     "style": "oblique",
#     "weight": "bold"
# }

# categories = ['A', 'B', 'C']
# values = [10, 15, 7]
# # plt.bar(categories, values)
# bars = plt.bar(categories, values, color=['r','g','b'], label="막대 샘플")
# plt.xticks(categories, ['2023', '2024', '2025'])

# for bar in bars:
#     plt.text(bar.get_x() + bar.get_width()/2,  # x좌표(막대의 중심)
#              bar.get_height() + 0.5,           # y좌표
#              str(bar.get_height()),
#              ha="center", va="top", color="black")

# plt.legend()
# plt.title("막대그래프 연습", pad=20)
# plt.xlabel("카테고리")
# plt.xticks(categories, ['2023', '2024', '2025'])
# plt.ylabel("수치")
# plt.show()
# -----------------------------------------------------------
# 수평 막대 그래프
font = {
    "size": 15,
    "color": "red",
    "style": "oblique",
    "weight": "bold"
}
categories = ['A', 'B', 'C']
values = [10, 15, 7]

bars = plt.barh(categories, values, color=[
                '#2233ff', '#ff2233', '#22ff33'], edgecolor="black")

for bar in bars:
    plt.text(bar.get_width() + 0.5,  # x좌표
             bar.get_y() + bar.get_height()/2,
             str(bar.get_width()),
             ha="right", va="center", color="green")  # y좌표 막대 중심

plt.legend(bars, ["A-2023", "B-2024", "C-2025"])
# 기준선
plt.axvline(x=values[2], linestyle="--", color="black")

plt.title("막대그래프 연습", pad=20)
plt.xlabel("카테고리")
plt.ylabel("수치")

# plt.show() 창띄우기
# 저장
plt.savefig("./1209/graph.jpg", format="jpg")
