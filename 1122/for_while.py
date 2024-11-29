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

"""
       if num.isdecimal() == True:
           num = int(num)
       else:
           print("양수만 입력하세요")
           continue
       if num < 0:
           print("양수만 입력하세요")
           continue
   """
'''
 # 실습.while문
 while True:
     num = input("숫자를 입력하시오 ,(종료를 원하시면 종료를 입력하세요) : ")
     count = 0
     total = 0
     if num == "종료":
         break
     if not num.isdigit():  # 음수 문자열은 무조건 False
         print("양수만 입력하세요")
         continue
     num = int(num)
     if num == 0:
         continue
     while count <= num:
         total += count
         count += 1
     print(f"1부터 {num}까지의 합은 {total}입니다.")

 print("프로그램이 종료되었습니다.")
 '''
'''
for i in range(10):
    print(i, end=" ")
print()
for i in range(3, 9):
    print(i, end=" ")
print()
for i in range(1, 100, 12):
    print(i, end=" ")
'''
'''
fruits = ['사과', '바나나', '포도', '체리']
for fruit in fruits:
    print(fruit, end=" | ")
'''
'''
# 합계 구하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for num in numbers:
    total += num
print(f"합계는 {total}입니다")


# 조건문 사용
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 != 0:
        print(num, end=" ")
'''

for i in range(1, 3, 1):
    print()
    print(f"{i}", end=" ")
    for j in range(1, 4, 1):
        print(f"{j}", end=" ")
