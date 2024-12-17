import folium
import requests
import pandas as pd

API_KEY = "e991276e7b1ef1338c588c40a840e884"


def get_weather_date(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=kr"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return None


cities = [
    {'name': '서울', 'lat': 37.5665, 'lon': 126.9780},
    {'name': '부산', 'lat': 35.1796, 'lon': 129.0736},
    {'name': '대전', 'lat': 36.3504, 'lon': 127.3845},
    {'name': '대구', 'lat': 35.8714, 'lon': 128.6014}
]
# 날씨데이터 리스트
weather_data=[]

for city in cities:
    data = get_weather_date(city["lat"], city['lon'])
    if data:
        weather_data.append({
            'city':city['name'],
            'temperature' : data['main']["temp"],
            'weather' : data['weather'][0]['description'],
            'Latitude' : city["lat"],
            "longitude" : city['lon']
        })

weather_df = pd.DataFrame(weather_data)
print(weather_df)

my_map = folium.Map(location=[36.5, 127.5], zoom_start=7)

# 마커 추가
for _ , row in weather_df.iterrows():
    popup_info = f"""
    <b>도시:</b> {row['city']}<br />
    <b>온도:</b> {row["temperature"]}℃<br />
    <b>날씨:</b> {row["weather"]}
    """
    # 날씨에 따라서 마커 색상
    icon_color ="blue" if row["temperature"] < 0 else "lightblue"

    # 마커 생성
    folium.Marker(
        location=[row["Latitude"], row["longitude"]],
        popup= folium.Popup(popup_info,max_width=300),
        icon = folium.Icon(color=icon_color,icon="cloud")
    ).add_to(my_map)

    my_map.save("./1217/my_map.html")