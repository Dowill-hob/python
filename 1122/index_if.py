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
