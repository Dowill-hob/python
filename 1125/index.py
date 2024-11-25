'''
# 리스트 반복
fruits = ["사과", "바나나", "체리"]
for fruit in fruits:
    print("과일은: ", fruit)  # 사과 바나나 체리

# 합계구하기
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"합계는 {total}입니다.")  # 합계는 15입니다.

# 조건문 사용하기
numbers = [1, 3, 5, 7, 9, 11]
for num in numbers:
    if num > 5:
        print(num, end=" ")  # 7 9 11
print()
# 조건문 사용
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in number:
    if num % 2 == 0:
        print(num, end=" ")
'''
'''
# 리스트 내포
squares = [x ** 2 for x in range(1, 20)]
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]

# if문과 함께사용
even_squares = [i ** 2 for i in range(1, 10) if i % 2 == 0]
print(even_squares)  # [4,16,36,64]
'''
'''
# 딕셔너리와 for문
my_dic = {
    "name": "홍길동",
    "address": "서울시 은평구",
    "gender": "남자",
    "hobby": ["런닝", "헬스", "낚시"]
}
'''
'''
# key값만 순회
for i in my_dic:
    print(i)
for i in my_dic.keys():
    print(i, end=" ")
print()
for i in my_dic.values():
    print(i, end=" ")
print()
'''
'''
for key, value in my_dic.items():
    print(key, value, end=" ")
    print(f"{key}: {value}")

# Json = 딕셔너리
'''
'''
while True:
    num = input("몇단을 출력할까요?: ,(종료를 원하시면 종료를 입력해주세요.)")
    if num == "종료":
        break
    if not num.isdigit():  # 음수 문자열은 무조건 False
        print("양수만 입력하세요")
        continue
    num = int(num)
    for i in range(1, 10):
        print(f"{num} * {i} = {num * i}")
'''
'''
# 실습. 정수 합 계산
num = int(input("어디까지 계산할까요: "))
total = 0
for i in range(1, num+1, 2):
    if i % 2 != 0:
        total += i
print(f"1 부터 {num}까지의 홀수 합: {total}")
'''
'''
# 실습.평균값 구하기
student_dic = {
    "st1": [83, 92, 88],
    "st2": [90, 79, 86],
    "st3": [88, 86, 94]
}
for key, value in student_dic.items():
    avg = sum(value)/len(value)
    print(f"{key}의 국,영,수과목 평균은 {avg:.4}점 입니다.")
'''
'''
# 실습.평균값 구하기
student_dic = {
    "st1": {
        "korean": 83,
        "english": 92,
        "math": 88
    },
    "st2": {
        "korean": 90,
        "english": 79,
        "math": 86},
    "st3": {
        "korean": 88,
        "english": 86,
        "math": 94
    }
}

for key, score in student_dic.items():
    total = sum(score.values())  # 세 과목의 합계
    avg = total / len(score)
    print(f"{key}의 평균은 {avg:.2f}")
'''
'''
# 이중 for문
for i in range(5):
    for j in range(3):
        print(f"i :{i}, j :{j}")
    print()
'''
'''
# 2차원리스트와 For문
matrix = [
    [3, 6, 9, 12],
    [2, 4, 8, 16],
    [5, 25, 125, 100],
    [11, 12, 13, 14]
]
for row in matrix:
    for element in row:
        if element % 3 == 0:
            print(element)
'''
'''
# 실습. 이중 for문 구구단 만들기
for i in range(2, 10):
    print(f"[{i} 단]")
    for j in range(1, 10):
        print(f"{i} x {j} = ", i*j)
    print()
'''
# 실습. 자판기 프로그램
vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '이프로']
while True:
    user = input("사용자 종류를 입력하세요: \n1.소비자\n2.주인\n3.종료\n")
    if user == '3':
        break
    if int(user) == 1:
        while True:
            brg = input("마시고 싶은 음료는: (없으실 경우 종료를 입력해 주세요)")
            if brg == '종료':
                break
            if brg in vending_machine:
                print(f"{brg} 드릴게요")
                vending_machine.remove(brg)
                print(f"남은 음료수:{vending_machine}")
            else:
                print("죄송합니다. 해당음료는 자판기에 없습니다.")
                continue
    elif int(user) == 2:
        opt = input("할 일 선텍:\n1. 추가\n2. 삭제\n3. 종료\n")
        if opt == '1':
            while True:
                print(f"남은 음료수:{vending_machine}")
                print()
                brg_add = input("추가할 음료? 또는 종료")
                if brg_add == '종료':
                    break
                vending_machine.append(brg_add)
                vending_machine.sort()
                print("추가 완료")
                print(f"남은 음료수:{vending_machine}")
        elif opt == '2':
            while True:
                print(f"남은 음료수:{vending_machine}")
                brg_remove = input("삭제할 음료수? 혹은 종료 ")
                if brg_remove == '종료':
                    break
                if brg_remove in vending_machine:
                    vending_machine.remove(brg_remove)
                    print("삭제완료")
                    print(f"남은 음료수:{vending_machine}")
                else:
                    print("자판기에 없는 음료입니다.")
        elif opt == '3':
            break
    else:
        print("1, 2, 3중 하나만 선택하십시오.")
        continue
