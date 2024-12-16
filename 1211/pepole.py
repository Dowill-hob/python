import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager
path = "C:\\Windows\\Fonts\\Hancom Gothic Bold.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)
# =======================================================================

'''
file_name = "./1211/202411_202411_연령별인구현황_월간.csv"
data = pd.read_csv(file_name, encoding="EUC-KR")


region_name = input("검색하고 싶은 지역명을 입력하세요: ")
data = data.rename(columns={'행정구역': '지역명'})
age_columns = [col for col in data.columns if "세" in col]  # '세' 가 있는 거만 필터링

# 숫자로 변환
for col in age_columns:
    data[col] = data[col].str.replace(",", "").astype(int)
print(data.head())
# 필터링
# contains() : 문자열 데이터 필터링, 특정 패턴을 찾을때
# na : 결측(NaN)값을 포함할지 결정, 기본값 True
# case : 영문의 대소문자 구분. 기본값 True
region_data = data[data["지역명"].str.contains(region_name, na=False)]

if region_data.empty:
    print(f"{region_name}의 지역은 존재하지 않습니다.")

# data 추출
age_groups = [col.split("_계_")[1] for col in age_columns]
region_data[age_columns].iloc[0]  # key values 형태
result = region_data[age_columns].iloc[0].values

# 그래프그리기
plt.figure(figsize=(10, 8))
plt.plot(age_groups, result, marker="*", label=region_name)
plt.title(f"{region_name}의 연령별 인구 수", fontsize=16, pad=10)
plt.xlabel("연령대")
plt.ylabel("인구수")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45)
plt.show() # savefig
'''
# =======================================================================
# 실습 지역의 연령대별 남성 및 여성 인구 비교

# 지역별 인구수 숫자화


def pepole_Data(age_columns, data):
    for col in age_columns:
        data[col] = data[col].astype(str).str.replace(",", "").astype(int)
# 나이별 인구수 함수


def age_data(data, txt1, txt2):
    # [col for col in region_data.filter(like="난_").colimns if "총인구수" not in col and "연령구간인구수" not in col]
    return [col for col in data.columns if txt1 in col and txt2 in col]
# 연령,성별 별 인구수


def result_data(data, age_data):
    # data[age_data].iloc[0].apply(lambda x : int(str(x).replace(",","")))
    return data[age_data].iloc[0].values
# x축


def split_data(data, txt1):
    return [col.split(txt1)[1] for col in data]


file_name = "./1211/연령별인구현황_월간.csv"
region_name = input("지역명을 입력하세요: ")
data = pd.read_csv(file_name, encoding="EUC-KR")
data = data.rename(columns={"행정구역": "지역명"})
age_columns = [col for col in data.columns if "세" in col]  # '세' 가 있는 거만 필터링

pepole_Data(age_columns, data)
# 지역 데이터
region_data = data[data["지역명"].str.contains(region_name, na=False)]
if region_data.empty:
    print(f"{region_name}은 존재하지 않습니다.")

age_male_columns = age_data(region_data, "남", "세")
age_female_columns = age_data(region_data, "여", "세")

age_male_groups = split_data(age_male_columns, "_남_")
result_male = result_data(region_data, age_male_columns)

age_female_groups = split_data(age_female_columns, "_여_")
result_female = result_data(region_data, age_female_columns)

# 그래프그리기
plt.figure(figsize=(10, 8))
plt.plot(age_male_groups, result_male, marker="o", label="남성", color="#2233ff")
plt.plot(age_female_groups, result_female, marker="o",
         label="여성", alpha=0.5, color="#d123c4")
plt.xlabel("연령대")
plt.ylabel("인구수")
plt.title(f"{region_name}의 연령대별 남성 및 여성 인구 비교", fontsize=16, pad=10)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6, color="orange")
plt.xticks(rotation=45)
plt.show()
