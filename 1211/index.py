import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import font_manager
from pydataset import data
path = "C:\\Windows\\Fonts\\Hancom Gothic Bold.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)
mtcars = data('mtcars')
# ======================================================================
# 종합 실습 (데이터 분석 후 그래프 그리기)
'''
# 1-1
avg_mpg = mtcars.groupby('cyl')['mpg'].mean().reset_index()
sns.barplot(data=avg_mpg, x='cyl', y='mpg', hue='cyl')
plt.show()
print(mtcars.head())
'''
'''
# 1-1-1
avg_mpg = mtcars.groupby('cyl')['mpg'].mean()
avg_mpg.plot(kind="bar")
plt.xticks(rotation=0)
plt.show()
'''
# ======================================================================
'''
# 1-2
avg_hp = mtcars.groupby('am')['hp'].mean().reset_index()
sns.barplot(data=avg_hp, x='am', y='hp', hue='am')
plt.title("변속기 유형별 평균 마력")
plt.show()
'''
'''
# 1-2-1
avg_hp = mtcars.groupby('am')['hp'].mean()
avg_hp.plot(kind="bar")
plt.xticks(rotation=0)
plt.show()
'''
# ======================================================================
'''
# pivot() 중복된 조합이 있을경우 오류 발생, 고유한 값이 보장될때 사용
# pivot_table() 중복된 조합이 있는 경우에도 동작, 실무에 더 적합
# 1-3
print(mtcars.head())
data = mtcars.pivot_table(index='cyl', columns='gear',
                          values='mpg')
sns.heatmap(data=data, annot=True, fmt=".1f", cmap="coolwarm")
plt.title("실린더 수을 기준으로 기어수에 따른 평균 연비")
plt.show()
'''
'''
# 1-3-1
avg_data = mtcars.groupby(['cyl', 'gear'])['mpg'].mean().reset_index()
data = avg_data.pivot(index='cyl', columns='gear',
                      values='mpg')
sns.heatmap(data, annot=True, fmt=".1f", cmap="coolwarm")
plt.title("실린더 수을 기준으로 기어수에 따른 평균 연비")
plt.show()
'''
# ======================================================================
'''
# corr(method="pearson" ) # 피어슨 상관계수(기본값)
# corr(method="spreaman" ) # 스피어만 상관계수
# corr(method="kendall") # 켄달의 타우 상간계수
# 1-4
data = mtcars[['mpg', 'hp', 'wt']] # 데이터 선택
data_heat = data.corr()
sns.heatmap(data_heat, annot=True, fmt=".2f", cmap='coolwarm')
plt.show()
'''
# ======================================================================
