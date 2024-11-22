'''
# while 문
i = 0
while i < 3:
    print("반복문", i)
    i += 1
print("종료")
'''
'''
# 합계 구하기
num = 1
total = 0
while num <= 10:
    total += num
    num += 1
print(f"1부터 10까지의 합은 {total}입니다.")
'''
'''
# 입력값 받기
user_input = ""
while user_input != "종료":
    user_input = input("원하는 값을 입력하세요. 종료하려면 '종료'를 입력하세요: ")
    print(f"입력한 값: {user_input}")
print("프로그램이 종료되었습니다.")
'''

# 실습.while문
while True:
    num = input("숫자를 입력하시오: ,(종료를 원하시면 종료를 입력하세요)")
    count = 0
    total = 0
    if num == "종료":
        break
    if num.isdecimal() == True:
        num = int(num)
    else:
        print("양수만 입력하세요")
        continue
    if num < 0:
        print("양수만 입력하세요")
        continue
    if num == 0:
        continue
    while count <= num:
        total += count
        count += 1
    print(f"1부터 {num}까지의 합은 {total}입니다.")
    user_input = input("다시 실행은 실행을, 종료는 종료를 입력해주세요: ")
    if user_input == "실행":
        continue
    if user_input == "종료":
        break
print("프로그램이 종료되었습니다.")
