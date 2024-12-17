
from geojson import Feature, FeatureCollection, Point, Polygon
import pandas as pd
import folium


# =====================================================================
'''
# 지도 열기
my_map = folium.Map(location=[37.608438, 126.919449], zoom_start=12)
my_map.save("./1217/my_map.html")
'''
# =====================================================================

# # 지도 스타일 추가
# # OpenStreetMap, CartoDB Positron,CartoDB Dark_Matter
# my_map = folium.Map(location=[37.608438, 126.919449],
#                     zoom_start=12, tiles='CartoDB Positron')
# my_map.save("./1217/my_map.html")

# =====================================================================
# my_map = folium.Map(location=[37.608438, 126.919449],zoom_start=12, tiles='CartoDB Positron')
# my_map = folium.Map(location=[37.608438, 126.919449], zoom_start=12,
#                     tiles="https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", attr="Google")

# folium.Marker([37.608438, 126.919449], popup="경복궁").add_to(my_map)  # 기본 마커
# folium.Marker([37.576936, 126.944588], popup="안산", icon=folium.Icon(
#     color="red", icon="home")).add_to(my_map)  # 기본 마커
# =====================================================================
'''
# 영역 표시
my_map = folium.Map(location=[37.517584, 127.126269],
                    zoom_start=13, tiles="CartoDB Positron")
# 원형 영역
folium.Circle(location=[37.515519, 127.128387],
              radius=500, color="purple", popup="올림픽 테니스 경기장", fill=True, fill_color="yellow").add_to(my_map)
my_map.save("./1217/my_map.html")
'''
# =====================================================================
'''
# 지도 생성
# 딕셔너리 형태로 여러개 추가
my_map = folium.Map(location=[37.517584, 127.126269],
                    zoom_start=13, tiles="CartoDB Positron")

map_info = [
    {"location": [37.516343, 127.131017], "popup": "KCI 올림픽공원역"},
    {"location": [37.515982, 127.123876], "popup": "지샘터올림픽공원도서관"},
    {"location": [37.520125, 127.129072], "popup": "성내천"}
]

for info in map_info:
    folium.Marker(location=info["location"], popup=info["popup"], icon=folium.Icon(
        color="green", icon="star")).add_to(my_map)

my_map.save("./1217/my_map.html")
'''
# =====================================================================

# 실습. folium 실습 문제
# my_map = folium.Map(location=[37.557408, 127.021539],
#                     zoom_start=15, tiles="CartoDB Positron")
# subway = [
#     {'location': [37.560207, 127.013902], 'popup' : '청구역'},
#     {'location': [37.554423, 127.020900], 'popup' : '신금호'},
#     {'location': [37.557412, 127.029658], 'popup' : '행당'},
#     {'location': [37.554411, 127.010981], 'popup' : '약수역'},
#     {'location': [37.564374, 127.029481], 'popup' : '상왕십리'}
# ]
# subway = {
#     'location': ['청구역', '신금호', '행당', '약수역', '상왕십리'],
#     '경도': [37.560207, 37.554423, 37.557412, 37.554411, 37.564374],
#     '위도': [127.013902, 127.020900, 127.029658, 127.010981, 127.029481]
# }
# map_info = pd.DataFrame(subway)
# for info in map_info.values:
#     folium.Marker(location=[info[1], info[2]], popup=info[0], icon=folium.Icon(
#         color="green", icon="star")).add_to(my_map)
#     folium.Circle(location=[info[1], info[2]], popup=info[0],
#                   fill=True, fill_color="yellow").add_to(my_map)
# map_info.apply(
#     lambda : folium.Marker(
#         location = [x["경도"],x["위도"]],
#         popup=x["location"],
#         icon=folium.Icon(color="blue" , icon="star")
#     ).add_to(my_map),
#     axis= 1
# )

# for _, x in map_info.iterrows():
#     folium.Marker(
#         location=[x["경도"], x["위도"]],
#         popup=x["location"],
#         icon=folium.Icon(color="blue", icon="star")).add_to(my_map)

# my_map.save("./1217/my_map.html")

# =====================================================================
'''
# geojson & folium
# GeoJSON 데이터 생성 (속성 추가 : name과 population)
feature1 = Feature(geometry=Point((126.9780, 37.5665)),
                   properties={"name": "서울", "population": "970만"})
feature2 = Feature(geometry=Point((129.0736, 35.1796)),
                   properties={"name": "부산", "population": "340만"})
feature3 = Feature(geometry=Point((127.3845, 36.3504)),
                   properties={"name": "대전", "population": "150만"})
feature4 = Feature(geometry=Point((128.6014, 35.8714)),
                   properties={"name": "대구", "population": "240만"})
# FeatureCollection으로 묶기 (list 형태태)
geojson_data = FeatureCollection([feature1, feature2, feature3, feature4])

# Folium 지도 생성
my_map = folium.Map(location=[36.5, 127.5], zoom_start=7)

# GeoJSON 데이터를 지도에 추가하고 툴팁 설정
folium.GeoJson(
    geojson_data,
    name="GeoJSON Layer",
    tooltip=folium.GeoJsonTooltip(
        fields=['name', 'population'],  # 표시할 속성 필드
        aliases=["도시 이름 : ", "인구 : "],  # 속성성에 대한 별칭
        localize=True
    )
).add_to(my_map)


my_map.save("./1217/my_map.html")
print("지도 저장 완료: my_map.html")
'''
# =====================================================================

# 실습. GeoJSON 실습
fields = [[
    [126.794997, 37.870247],
    [126.517592, 37.502918],
    [126.637069, 37.227869],
    [126.803978, 37.146663],
    [127.228942, 37.220265],
    [127.294766, 37.403040],
    [127.231252, 37.662200],
    [127.081128, 37.737124],
    [126.794997, 37.87024]
]]

my_map = folium.Map(location=[37.551452, 126.988963], zoom_start=7)

field = Feature(geometry=Polygon(fields), properties={'name': '수도권'})

geojson_data = FeatureCollection([field])

folium.GeoJson(
    geojson_data,
    name="GeoJSON Layer",
    tooltip=folium.GeoJsonTooltip(
        fields=['name'],
        aliases=['영역 이름 : '],
        localize=True
    ),
    style_function=lambda x: {
        'fillColor': 'yellow',  # 다각형 내부 색상
        'color': 'black',  # 테두리 색상
        'weight': 2,  # 테두리 두께
        'fillOpacity': 0.5  # 내부 투명도
    }
).add_to(my_map)

my_map.save("./1217/my_map.html")
print("지도 저장 완료")
