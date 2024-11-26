weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0],
]
# for record in weather_data[0:]:  # 제목 행 제외
#     city = record[1]
#     rainfall = record[3]
#     if rainfall > 0:
#         if city in weather_data:
#             rainy_days += 1
#         else:
#             rainy_days = 1


def Count_rainy_days(data):
    for record in data[0:]:  # 제목 행 제외
        city = record[1]
        rainfall = record[3]
        if rainfall > 0:
            if city in weather_data:
                rainy_days += 1
            else:
                rainy_days = 1


city = '서울'
rainy_days = Count_rainy_days(weather_data)
print(f"{city}에서 비가 내린 날: {rainy_days}일")
