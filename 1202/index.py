import requests
import json
url = " https://koreanjson.com/posts"

respond = requests.get(url)  # post 면 post

if respond.status_code == 200:
    data = respond.json()
    for i in data:
        print(f"ID: {i['id']}, 제목: {i['title']}")

else:
    print("요청 실패")

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

try:
    # 예외가 발생할 가능성이 있는 코드
    x = int(input("숫자를 입력하세요: "))
    result = 10 / x
# except ZeroDivisionError as e:
#     print("예외메세지: ", e)
# except ValueError as e:
#     print("예외메세지: ", e)
except (ValueError, ZeroDivisionError) as e:
    print("예외 발생: ", e)
else:
    # 예외가 발생하지 않았을 때 실행
    print("결과: ", result)
finally:
    # 예외 발생 여부와 상관없이 항상 실행
    print("프로그램이 종료됩니다.")


class Car:

    def __init__(self, model, cc):
        self.model = model
        self.cc = cc

    def __str__(self):
        return f"model: {self.model}, cc: {self.cc} cc"


car1 = Car("아반떼", 1000)  # 인스턴스 생성
print(car1)
# model: 아반떼, cc: 1000 cc
