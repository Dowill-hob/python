'''
# 모듈
# import calc
# import calc as a
# from calc import add, sub
# from calc import add as a, sub as b
from calc import *
# 모듈명.함수명
print(add(10, 4))
print(sub(10, 4))
print(mul(10, 4))
print(div(10, 4))
'''

'''
now = datetime.today()
print(now)  # 현재시간
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

print(f"{now.year}년 {now.month}월 {now.day}일")
'''
'''
from datetime import datetime, timedelta, timezone
now = datetime.now()
print(now)
print(now.year)

# 특정 날짜 계산
next_week = now + timedelta(weeks=1, hours=1)
print(next_week)

# 타임존 계산
print(timezone.utc)
print(datetime.now(timezone.utc))

print(datetime.now(timezone(timedelta(hours=9))))

'''

'''
from datetime import date
open_day = date(year=2024, month=11, day=18)
print(date.today())
week = ['월', '화', '수', '목', '금', '토', '일']
print(week[date.today().weekday()])  # 요일
pass_day = date.today() - open_day
print(pass_day.days)
'''
'''
print(time.time())
print(time.localtime())
# print("2초 대기")
# time.sleep(2)
# print("대기완료")
start = time.perf_counter()  # 시간 측정
time.sleep(1)
end = time.perf_counter()
print(end - start)
'''


# print(math.pi)
# print(math.sqrt(49))
# print(math.factorial(5))
'''
print(math.ceil(2.43))   # 올림
print(math.floor(4.88))  # 버림
print(round(3.5))        # 반올림
'''


# print(random.randint(1, 10))
# print(random.uniform(1.1, 5.5))
# print(random.random())
# print(random.randrange(1000, 10000))
# choices = [1, 2, 3, 4, 5, 6, 7, 8]
# print(random.choice(choices))

# rand = 1000 + math.floor(random.random() * 9000)
# print(rand)

# 실습.로또번호 뽑기
'''
import math
import random

lotto = random.sample(range(1, 46), 6)

print(sorted(lotto))

# num = set()
# while True:

#     if len(num) == 6:
#         break
#     for i in range(1):
#         ran = random.randint(1, 45)
#         num.add(ran)

# print(sorted(num))
'''
'''

import sys

# print(sys.argv)
# print(sys.argv[1:])

if "-h" in sys.argv or "--help" in sys.argv:
    print("사용법: python main.py")
    print("-h, --help         도움말 표시")
    print("-v, --version      버전정보표시")
    sys.exit(0)

if "-v" in sys.argv or "--version" in sys.argv:
    print("버전 : 1.0.0")
    sys.exit(0)

'''
'''
dir_current = os.getcwd() #디렉토리
print(dir_current)
file_path = os.chdir(dir_current) #경로이동
dir = os.popen('ls') #명령어 입력
print(dir.read()) #명령한 내용을 출력
# os.mkdir("test")
# os.rmdir("test")

# import os
# print(os.environ.get('PATH'))
import json
data = {
    "name": "홍길동",
    "age": 20,
    "city": "서울"
}
json_str = json.dumps(data)
print(json_str)

json_obj = json.loads(json_str)
print(json_obj["name"])
'''


# user_insert = input("영단어 타자 테스트 시작하시겠습니까? (실행 or 종료): ")




import time
import random
def game():
    if user_insert == "실행":
        print("종료 명령어는 exit입니다.")
        start = time.perf_counter()
        typing_test = ['apple', 'mountain', 'dish', 'paradox', 'cloud', 'rain', 'japan', 'kingdom', 'coding', 'sleep',
                       'korea', 'paragraph', 'word', 'unpleasant', 'upset', 'sad', 'fun', 'kind', 'like', 'lie']
        count = 0
        while True:
            count += 1
            print()
            word = random.choice(typing_test)
            print(f"단어: {word}")
            typing = input("입력: ")
            if typing == word:
                print("통과")
                continue
            elif typing == "exit":
                end = time.perf_counter()
                print("게임종료!")
                print(f"총 {count-1}개의 단어를 입력했습니다.")
                print(f"총 걸린 시간: {end-start:.2f}초")
                print(f"평균 단어당 입력 시간: {(end-start)/(count-1):.2f}초")
                break
            else:
                print("오타! 다시 시도하세요.")
                print(f"단어: {word}")
                re_insert = input("입력: ")
                if re_insert == word:
                    print("통과")
                    continue
                else:
                    end = time.perf_counter()
                    print("2번 연속 틀렸으므로 프로그램을 종료합니다.")
                    print(f"총 {count-1}개의 단어를 입력했습니다.")
                    print(f"총 걸린 시간: {end-start:.2f}초")
                    print(f"평균 단어당 입력 시간: {(end-start)/(count-1):.2f}초")
                    break

    elif user_insert == "종료":
        print("프로그램이 종료되었습니다.")
    else:
        print("다시 입력해주세요.")


user_insert = input("영단어 타자 테스트 시작하시겠습니까? (실행 or 종료): ")
game()
