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
# 실습.elif

score = int(input("점수를 입력하세요 : "))

if score >= 90:
    print("학점 : A")
elif score >= 80:
    print("학점 : B")
elif score >= 70:
    print("학점 : C")
elif score >= 60:
    print("학점 : D")
else:
    print("학점 : F")
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


# 삼항연산자

age = int(input("나이를 입력히세요"))
message = "20대입니다" if age < 30 and age >= 20 else "20대가 아닙니다."
print(message)
