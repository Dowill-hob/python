import pandas as pd
'''
# 리스트형식으로 생성
data = [10, 20, 30, 40]
# series = pd.Series(data)
series = pd.Series(data, index=["a", "b", "c", "D"])
print(series)


# 딕셔너리형식으로 생성
data = {
    "a": 10,
    "b": True,
    "C": 3.14,
    "d": "python"
}
series = pd.Series(data, name="딕셔너리")
# print(series)
# print(series.index)
# print(series.values)
# print(series.shape)
'''
'''
data = ('민지', '여', False)
member = pd.Series(data, index=['이름', '성별', '결혼여부'])
print(member)
print(member['이름'])
print(member[['성별', '결혼여부']])

data = [10, 20, 30, 40, 50]
series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
# print(series[0])
print(series[series > 20])
series['c'] = 100
print(series)
'''
# =======================================================================================================
'''
# 실습 시리즈 만들기
data = ["4 cups", "1 cup", "2 large", "1 can"]
series = pd.Series(data, index=['밀가루', '우유', '계란', '참치캔'], name="Dinner")
print(series)
'''
# =======================================================================================================

# 데이터 프레임
data = {
    'Name': ['홍길동', '임꺽정', '성춘향'],
    'Age': [25, 30, 27],
    'City': ['서울', '부산', '인천']
}
df = pd.DataFrame(data)
print(df)
