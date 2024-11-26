'''
minus = (lambda x, y: x-y)
print(minus(10, 2))
print((lambda x, y: x-y)(7, 4))

'''

'''
def call(func):
    for _ in range(10):
        func()


def hello():
    print("안녕하세요")


hello2 = (lambda: print("반갑습니다."))
call(hello2)
'''
'''
numbers = [2, 4, 6, 8]
squered = map(lambda x: x ** 3, numbers)
print(list(squered))
'''
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda x: x % 2 == 0, numbers)))
'''
# 방법 3 중첩함수를 쓰는 방법

'''
def count(num):
    lists = list(filter(lambda x: x % num == 0, range(1, 31)))
    return lists, len(lists)


num = 5
lists, counts = count(num)
print(f"{num}의 배수: {lists}")
print(f"{num}의 개수: {counts}")
'''

# 실습6.함수 종합 프로그래밍
weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0],
]


def Count_rainy_days(data, city):
    rainy_days_count = 0
    for record in data[0:]:
        city_name = record[1]
        rainfall = record[3]
        if city_name == city and rainfall > 0:
            rainy_days_count += 1  # 비가 내린 날 증가

    return rainy_days_count


def city_insert(city):
    return list(filter(lambda weather_data: weather_data[1] == city, weather_data))


def temp_map(city):
    return list(map(lambda weather_data: weather_data[2], city_insert(city)))


def rain_map(city):
    return list(map(lambda weather_data: weather_data[3], city_insert(city)))


print(
    "[날씨 데이터 분석 프로그램]\n"
    "1. 평균 기온 계산\n"
    "2. 최고/최저 기온 찾기\n"
    "3. 강수량 분석\n"
    "4. 날씨 데이터 추가\n"
    "5. 전체 데이터 출력\n"
    "6. 종료"
)
while True:
    user_insert = int(input("원하는 기능의 번호를 입력하세요: "))
    if user_insert == 6:
        break
    elif user_insert == 1:
        city = input("도시 이름을 입력하세요: ")
        city_insert(city)
        avg_temp = sum(
            list(map(lambda weather_data: weather_data[2], city_insert(city))))/len(city_insert(city))
        print(f"{city}의 평균 기온은 {avg_temp:.2f}도 입니다.")
        print()
    elif user_insert == 2:
        city = input("도시 이름을 입력하세요: ")
        city_insert(city)
        temp_max = max(temp_map(city))
        temp_min = min(temp_map(city))
        print(f"{city}의 최고 기온은 {temp_max}도 이고 최저 기온은 {temp_min}도 입니다.")
        print()
    elif user_insert == 3:
        city = input("도시 이름을 입력하세요: ")
        city_insert(city)
        total_rain = sum(rain_map(city))
        print(f"{city}의 총 강수량: {total_rain}mm")
        rainy_days = Count_rainy_days(weather_data, city)
        print(f"{city}에서 비가 내린 날: {rainy_days}일")
        print()
    elif user_insert == 4:
        date = input("날짜를 입력하세요 (yyyy-mm-dd): ")
        city = input("도시 이름을 입력하세요: ")
        temp = input("평균 기온을 입력하세요(℃): ")
        rain = input("강수량을 입력하세요(mm): ")
        add = [date, city, temp, rain]
        weather_data.append(add)
        print(f"{city}의 날씨 데이터가 추가되었습니다.")
        print()
    elif user_insert == 5:
        for record in weather_data[0:]:
            print(
                f"날짜: {record[0]}, 도시: {record[1]}, 평균 기온: {record[2]}℃, 강수량: {record[3]}mm")
        print()
