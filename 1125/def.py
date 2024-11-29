'''
# 함수

def say_hello(born, name):
    age = 2024 - born
    print(f"{name}의 나이는 {age}세입니다.")


say_hello(1700, '누군가')
say_hello(2000, '홍길동')
say_hello(2001, "아무개")

# multiple함수


def gugudan(dan, end):
    print(f"{dan}단")
    for i in range(1, end+1):
        print(f"{dan} x {i} = {dan * i}")


gugudan(4, 20)
gugudan(7, 50)
'''
'''
# 결과값이 있는 함수


def calc_sum(num1, num2):
    total = 0
    for i in range(num1, num2+1):
        total += i

    return total


result = calc_sum(10, 20)
print(result)
'''
'''

def fruits():
    return ["사과", "바나나", "복숭아"]


print(fruits())


def student_info():
    return {
        "name": "아무개",
        "age": 25,
        "major": "컴퓨터공학"
    }


print(student_info())
'''
'''
# 실습


def sum_mult(num1, num2):
    if num1 == num2:
        print("결과(곱)= ", num1 * num2)
    else:
        print("결과(합)= ", num1+num2)
    return


sum_mult(2, 2)
sum_mult(2, 3)


# 실습 2


def delivery_charge(price):
    total = 0
    fee = 2500
    if price.isdecimal() == True:
        if price < 20000:
            total = price + fee
        else:
            total = price
    else:
        print("양수만 입력하세요")
    return (total)


delivery_charge('-15000')
'''
'''
# 함수 매개변수로 리스트 전달


def times(nums):
    return [i ** 2 for i in nums]


number = [2, 3, 6, 9]
print(times(number))
'''
vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '이프로']
'''


while True:
    user = input("사용자 종류를 입력하세요: \n1.소비자\n2.주인\n3.종료\n")
    if user == '3' or "종료":
        break
    if int(user) == 1 or "소비자":
        while True:
            drink = input("마시고 싶은 음료는: (없으실 경우 종료를 입력해 주세요)")
            if drink == '종료':
                break
            is_drink(drink)
    elif int(user) == 2 or "주인":
        opt = input("할 일 선텍:\n1. 추가\n2. 삭제\n3. 종료\n")
        if opt == '1'or"추가":
            while True:
                check_machine()
                print()
                drink = input("추가할 음료? 또는 종료")
                if drink == "종료":
                    break
                add_drink(drink)
                vending_machine.sort()
                print("추가 완료")
        elif opt == '2'or "삭제":
            while True:
                check_machine()
                drink = input("삭제할 음료수? 혹은 종료 ")
                if drink == '종료':
                    break
                remove_drink(drink)
        elif opt == '3' or "종료":
            break
    else:
        print("1, 2, 3중 하나만 선택하십시오.")
        continue
'''

'''
def is_drink(drink):
    if drink in vending_machine:
        print(f"{drink}를 드릴게요")
    else:
        print(f"{drink}는 목록에 없습니다.")


def add_drink(drink):
    add = vending_machine.append(drink)
    return (add)


def remove_drink(drink):
    if drink in vending_machine:
        remove = vending_machine.remove(drink)
    else:
        print("목록에 없는 음료수 입니다.")
    return (remove)


def check_machine():
    check = print("남은 음료수:", vending_machine)
    return (check)


while True:
    user = input("사용자를 선택하세요")

    if user == "1" or user == "소비자":
        drink = input("원하시는 음료")
        is_drink(drink)
        check_machine()

    elif user == "2" or user == "주인":
        opt = input("무엇을 할 것입니까?")
        if opt == 1 or opt == '추가':
            drink = input("추가할 음료는?")
            add_drink()
        elif opt == 2 or opt == '삭제':
            drink = input("삭제할 음료는?")
            remove_drink()
        else:
            break
    else:
        break
'''
'''# 실습 구구단


def calculate_sum(end):
    total = 0
    for i in range(1, end+1):
        total += i
    return total


result = calculate_sum(10)
print(result)
'''


def times(num):
    return [i * 3 for i in num]


arr = [1, 2, 3, 4, 5]
newArr = times(arr)
print(newArr)  # [3,6,9,12,15]
