import pandas as pd

file_name = "./1209/서울특별시_공원 내 운동기구 설치 현황_20201231.csv"
df = pd.read_csv(file_name, encoding="cp949")
# park_equiments = df.groupby(' 구분 ')[' 운동기구 수량 '].sum()
# park_equiments.to_string("./1209/공원별 총 운동기구 설치 수.txt", index=True)

# equiments_data = df.groupby(' 운동기구 기종명 ')[' 운동기구 수량 '].sum()
# equiments_data.to_string("./1209/운동기구 종류별 설치개수.txt", index=True)

# management_agency_equiments = df.groupby(' 관리기관 ')[' 운동기구 수량 '].sum()
# management_agency_equiments.to_string(
#     "./1209/관리기관별 총 운동기수 설치 수.txt", index=True)

# park_info = df[df[' 구분 '] == ' 남산공원(회현) ']
# park_info.to_string("./1209/특정 공원 데이터 필터링.txt", index=False)


# equiments_info = df[df[' 운동기구 기종명 '] == ' 스텝사이클 ']
# equiments_info.to_string("./1209/운동기구 종류 데이터 필터링", index=False)

# data_easc = df.sort_values(' 운동기구 수량 ', ascending=False)
# data_easc.to_string("./1209/운동기구 수량 기준 내림차순.txt", index=True)
# =========================================================================================#
'''
# print(df.info())
# print(df.isnull().sum())

# print(df.columns)
df.columns = df.columns.str.strip()
park_count = df.groupby('구분')['운동기구 수량'].sum()
with open("./1209/park_counts.txt", "w", encoding="utf-8") as file:
    file.write("공원별 총 운동기구 설치수 \n")
    file.write(park_count.to_string())

equiment_count = df["운동기구 기종명"].value_counts()
with open("./1209/equiment_count.txt", "w", encoding="utf-8") as file:
    file.write("운동기구 별 설치수 \n")
    file.write(equiment_count.to_string())

management_count = df.groupby('관리기관')['운동기구 수량'].sum()
with open("./1209/management_count.txt", "w", encoding="utf-8") as file:
    file.write("관리기관 별 설치수 \n")
    file.write(management_count.to_string())

filter_park = df[df['구분'] == '남산공원(회현)']
with open("./1209/filter_park.txt", "w", encoding="utf-8") as file:
    file.write("남산공원(회현)  data \n")
    file.write(filter_park.to_string())

filter_equiment = df[df['운동기구 기종명'] == '스텝사이클']
with open("./1209/filter_equiment.txt", "w", encoding="utf-8") as file:
    file.write("스텝사이클 data \n")
    file.write(filter_equiment.to_string())

sort_df = df.sort_values(by="운동기구 수량", ascending=False)
with open("./1209/sort_df.txt", "w", encoding="utf-8") as file:
    file.write("운동기구 수량 내림차순 data \n")
    file.write(sort_df.to_string())
'''
