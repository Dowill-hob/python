'''
age = 21

if age < 20:
    print("미성년자 입니다")
else:
    print(f"나이는 {age}입니다")
'''
'''
# 실습.if~else
# 1
pwd = input("비밀번호를 입력하세요 : ")
if pwd == "abc123":
    print("비밀번호가 맞습니다.")
else:
    print("비밀번호가 틀렸습니다.")
# 2
num = int(input("숫자를 입력하세요 : "))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
'''
'''
# elif
age = int(input("나이를 입력하세요."))

if age < 20:
    print("10대입니다.")
elif age <30:
    print("20대입니다.")
elif age<40:
    print("30대입니다.")
elif age<50:
    print("40대입니다.")
else:
    print("50대입니다.")
'''
'''
'''
'''
# 실습.중첩 조건문
age = int(input("나이를 숫자로 입력해주세요 : "))
creadit = input("결제방법을 입력해주세요 (현금 또는 카드) : ")

if creadit == "카드":
    if age >= 0 and age < 75:
        if age < 8:
            print(f"{age}세의 카드 요금은 무료입니다.")
        elif age < 14:
            print(f"{age}세의 카드 요금은 450원 입니다.")
        elif age < 20:
            print(f"{age}세의 카드 요금은 720원 입니다.")
        elif age < 75:
            print(f"{age}세의 카드 요금은 1200원 입니다.")
    elif age >= 75:
        print(f"{age}세의 카드 요금은 무료입니다.")
    else:
        print("나이를 다시 확인해주세요")
elif creadit == "현금":
    if age >= 0 and age < 75:
        if age < 8:
            print(f"{age}세의 현금 요금은 무료입니다.")
        elif age < 14:
            print(f"{age}세의 현금 요금은 450원 입니다.")
        elif age < 20:
            print(f"{age}세의 현금 요금은 1000원 입니다.")
        elif age < 75:
            print(f"{age}세의 현금 요금은 1300원 입니다.")
    elif age >= 75:
        print(f"{age}세의 카드 요금은 무료입니다.")
    else:
        print("나이를 다시 확인해주세요")
else:
    print("결제방법을 다시확인해 주세요.")

'''
'''
# 삼항연산자

age = int(input("나이를 입력히세요"))
# message = "20대입니다" if age < 30 and age >= 20 else "20대가 아닙니다."
message = "20대입니다" if age < 30 and age >= 20 else "30대 입니다." if age < 40 and age >= 30 else "20대도 30대도 아닙니다."

print(message)
'''
'''
# 조건문에서 in연산자 활용
fruit = input("과일을 한글로 입력하세요: ")

if fruit in ["사과", "바나나", "복숭아"]:
    print(f"{fruit}은(는) 과일에 포함되어 있습니다.")
else:
    print("존재하지 않는 과일입니다.")
'''
'''
'''
'''
age = int(input("당신의 나이는?: "))
if age >= 20:  # 20 <= age 성인
    print("성인")
elif age >= 10:  # 10 <= age < 20 청소년
    print("청소년")
else:  # 위 조건에 전부 속하지 않는 경우
    print("어린이")

# 실습.elif

score = int(input("점수를 입력하세요 : "))

if score >= 90:
    pass
elif score >= 80:
    print("학점 : B")
elif score >= 70:
    print("학점 : C")
elif score >= 60:
    print("학점 : D")
else:
    print("학점 : F")
'''

'''age = int(input("나이를 입력해주세요: "))
adult_child = "성인입니다." if age > 19 else "미성년자입니다."
print(adult_child)
'''
# 실습.in연산자 활용
fruit_dict = {'apple': 95, 'banana': 105,
              'cherry': 50, 'strawberry': 58, 'grape': 3}
fruit_user = input(
    "Kcal을 알고싶은 과일을 영문으로 입력하세요\n"
    "(apple, banana, cherry, strawberry, grape): "
)
if fruit_user in fruit_dict:
    text = fruit_dict[fruit_user]
    print(f"{fruit_user}의 칼로리는 {text}Kcal입니다.")
else:
    print("포함되어있지 않은 과일입니다.")
