
# 함수 종합 프로그램
# 초기 날씨 데이터
weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울",  8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0],
]

# 평균 기온함수


def avg_temperatures(weather_data):
    city = input("도시 이름을 입력하세요: ")
    temp = filter(lambda x: x[1] == city, weather_data)
    temperatures = list(map(lambda x: x[2], temp))
    if not temperatures:
        return city, None
    else:
        return city, sum(temperatures)/len(temperatures)
# 최저/최고 기온함수


def max_min_temperatures(weather_data):
    city = input("도시 이름을 입력하세요: ")
    temp = filter(lambda x: x[1] == city, weather_data)
    temperatures = list(map(lambda x: x[2], temp))
    if not temperatures:
        return city, None, None
    else:
        return city, max(temperatures), min(temperatures)

# 강수량과 비온날 찾는 함수


def total_rain_Day(weather_data):
    city = input("도시 이름을 입력하세요: ")
    temp = filter(lambda x: x[1] == city, weather_data)
    rain = list(map(lambda x: x[3], temp))
    total_rain = sum(rain)
    rainy_days = len(list(filter(lambda x: x > 0, rain)))
    return city, total_rain, rainy_days
# 데이터 추가


def add_weather(weather_data):
    Date = input("날짜를 입력하세요 (YYYY-MM-DD): ")
    city = input("도시 이름을 입력하세요: ")
    temperatures = float(input("평균 기온을 입력하세요(℃ ): "))
    rain = float(input("강수량을 입력하세요 [mm]: "))
    return city
# 전체 데이터 출력함수


def all_weather_date(weather_data):
    print("\n현재 저장된 날씨 데이터")
    for data in weather_data:
        print(
            f"날짜: {data[0]}, 도시: {data[1]}, 평균기온: {data[2]}℃ , 강수량: {data[3]}mm")


def main_program():
    while True:
        print("\n[날씨 데이터 분석 프로그램]")
        print("1. 평균 기온 계산")
        print("2. 최고/최저 기온 찾기")
        print("3. 강수량 분석")
        print("4. 날씨 데이터 추가")
        print("5. 전체 데이터 출력")
        print("6. 종료")

        choice = input("원하는 기능의 번호를 입력하세요: ")
        if choice == '1':
            city, avg_result = avg_temperatures(weather_data)
            if avg_result is None:
                print(f"{city}의 정보가 존재하지 않습니다.")
            else:
                print(f"{city}의 평균 기온: {avg_result:.2f}℃")

        elif choice == '2':
            city, max_value, min_value = max_min_temperatures(weather_data)
            if max_value is none:
                print(f"{city}의 정보가 존재하지 않습니다.")
            else:
                print(f"{city}의 최고기온: {max_value}℃, 최저기온: {min_value}℃")

        elif choice == '3':
            city, total_rain, rainy_days = total_rain_Day(weather_data)
            print(f"{city}의 총 강수량: {total_rain:.1f}mm")
            print(f"{city}의 비가 온 날은: {rainy_days}일")

        elif choice == '4':
            city = add_weather(weather_data)
            print(f"{city}의 날씨 데이터가 추가되었습니다.")
        elif choice == '5':
            all_weather_date(weather_data)
        elif choice == '6':
            print("프로그램을 종료합니다.")
            break
        else:
            print("1~6까지의 번호를 입력하세요")


# 프로그램 정리 함수
main_program()
