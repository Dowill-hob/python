# 변수의 사이즈 알아보는 방법

"""
from sys import getsizeof
print(getsizeof(1))
print(getsizeof("1"))
"""

# 변수의 자료형 알아보는 방법

'''
print(type(1111))
print(type(333.333333333333333))
print(type("hello"))
print(type(True))
print(type(None))
'''

# 실습.연산자 연습
'''
num = input("숫자를 입력하세요: ")
a = float(num) % 2 == 0.0
print("True면 짝수, False면 홀수",a)
print(int(5.5))
a="30"
print(int("30"))
'''
'''
# 문자열 연산하기
a = "파이썬"
print("안녕하세요 " + a + " 반갑습니다.")
print("안녕하세요" , "반갑습니다.")
# print("오류" + 1234)

print("hey " * 10)

print("데이터 확인 ",a)
'''
# (''') 문자열 혹은 주석처리를 위해 사용
'''
korea_song = """ 
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로 길이 보전하세
"""
print(korea_song)
'''
'''
# 따옴표 출력
print("'오늘저녁 뭐먹지?'")
'''
'''
# 문자열 포매팅
print("올해는 2024년 용띠의 해이다")
year = "올해는 %d년 %s의 해이다" % (2024, "용띠")
year = "올해는 %d년 %s의 해이다" % (2025, "뱀띠")
print(year)
'''
'''
# 포맷코드 활용
number = "저는 올해 %d살 입니다." % 25
print(number)
calc = "20 나누기 3은 %.2f" % 6.66666666
print(calc)
text = "저는 %-10s에서 살고있습니다." % "서울"
print(text)
char = "이모티콘은 %c 이것으로 할께요" % "😎"
print(char)
'''
'''
country = "대한민국"
city = "서울"
people = "한국인"
text = "저는 올해 {0}살 입니다".format(25)
print(text)
text = "저는 {0} 사람이며 {1}에 살고있습니다.".format(country, city)
print(text)
text = "제가 사는 {0}은 {a}에 있습니다.".format(city, a="한국")
print(text)
text = "저는 {1}이다 {{그리고}}에 {0}에 살고있다.".format(country, people)
print(text)
text = "{}, {}, {}, {}".format(80,90,100,200)
print(text)
'''
'''
a = "[{0:<10}]".format("hey")
print(a) # 좌측정렬, 나머지 공백 [hey       ]
a = "[{0:>10}]".format("hey")
print(a) # 우측정렬, 나머지 공백 [       hey]
a = "[{0:^10}]".format("hey")
print(a) # 가운데정렬, 나머지 공백 [   hey    ]
a = "[{0:!<10}]".format("hey")
print(a) # 좌측정렬, 특수문자 [hey!!!!!!]
a = "[{0:^20.7f}]".format(1/3)
print(a) # 가운데정렬, 좌/우공백, 전체길이 20 [      0.3333333      ]
a = "[{0:,}]".format(123456789)
print(a) # 세자리 수 마다 [123,456,789]
'''
'''
# 이스케이프
print("Hello\nworld")
print("Hello\tWorld")
print("Hellp\\World")
print(' \'Hello\' ')
print(" \"Hello\" ")
'''
'''
# 실습. 이스케이프 연습
print('|\_/|\n|q p|   /}')
print('( 0 )"""\ ')
print('|"^"`    |')
print('||_/=\\\__|')
'''
'''
# f 문자열 포매팅
name = "홍길동"
age = 24
print(f"내이름은 {name}입니다. 나이는 {age + 1}입니다.")
print(f"내이름 [{name:@^20}]")
'''
'''
# 실습.f문자열 연습
name = "김준식"
print(f"[{name:=^11}]")
print(f"문자열 실습입니다. {{ 중괄호 }}를 출력해보세요.")
'''

python ="Hello, Python"
print(python[7:])

a="20240930"
print(a[:4]+"년",a[4:6]+"월",a[6:8]+"일")