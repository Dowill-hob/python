import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import font_manager

path = "C:\\Windows\\Fonts\\Hancom Gothic Bold.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)
# print(sns.get_dataset_names())

# 예제데이터
# tips = sns.load_dataset('tips')
# print(tips.head())
# =============================================================
# 산점도 분포시각화
# sns.scatterplot(x="total_bill",y="tip",hue="size",style="time",size="size",alpha=0.8,data=tips)
# sns.stripplot(x="day", y="total_bill", data=tips,jitter=True, hue="size", dodge=True)
# sns.swarmplot(x="day", y="total_bill", data=tips, hue="size", dodge=True)
# =============================================================
# 관계형 플롯 분포시각화
# sns.relplot(x="total_bill", y="tip", data=tips, style="time", hue="sex")
# =============================================================
# 카테고리형 데이터 분포시각화
# sns.catplot(x="day", y="total_bill", data=tips, hue="sex", kind="boxen")
# =============================================================
# 데이터 분포시각화
# sns.displot(tips['total_bill'], bins=30, kde=True)  # hist,ecdf,kde = 분포그래프 종류
# =============================================================
# 2차원 데이터(매트립스)를 히트맵 형식
# data = np.random.rand(10, 10)
# sns.heatmap(data, annot=True, fmt=".2f", cmap="coolwarm")
# =============================================================
# 여러 변수 간의 관계
# sns.pairplot(tips, hue="sex")
# =============================================================
# 회귀선이 포함된 산점도를 생성
# sns.regplot(x="total_bill", y="tip", data=tips)
# plt.show()
# =============================================================
# 실습 1
# penguins = sns.load_dataset('penguins')
# print(penguins.head())
# sns.catplot(x="island", y="body_mass_g",
#             data=penguins, hue="island", kind='violin')
# plt.show()
# =============================================================
# 실습 2
# flights = sns.load_dataset('flights')
# avg = flights.groupby('year')['passengers'].mean().reset_index()
# # reset_index() : 인덱스를 초기화, 기존 인덱스를 데이터프레임의 열로 뱐환
# plt.plot(avg["year"], avg['passengers'])
# plt.show()
# =============================================================
# 실습 2
# flights = sns.load_dataset('flights').pivot(
#     index='year', columns='month', values='passengers')
# print(flights.head())
# sns.heatmap(data=flights, annot=True, fmt=".2f", cmap="coolwarm")
# plt.title("연도와 월별 승객 수 히트맵")
# plt.show()
# =============================================================
# 실습 2
# flights = sns.load_dataset('flights')
# year_data = flights[flights['year'] == 1958]
# sns.barplot(data=year_data, x='month', y='passengers')
# plt.show()
# =============================================================
# 실습 3
# titanic = sns.load_dataset('titanic')
# sns.catplot(
#     data=titanic, x="class", y="survived", hue="sex",
#     kind='bar', height=4, aspect=.6)
# plt.title("탑승 클래스와 생존여부 관계")
# plt.show()
# =============================================================
# 실습 3
# titanic = sns.load_dataset('titanic')
# sns.kdeplot(data=titanic, x='age', hue='survived', fill=True)
# plt.grid(alpha=0.5, linestyle="--")
# plt.title("나이의 분포에 따른 셍존 여부 분포도")
# plt.show()
