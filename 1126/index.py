'''
# 전역변수
quantity = 10  # 고정된 값으로 많이 씀


def get_price(price):
    price = price * quantity
    return price


print(f"{quantity}개의 가격은 {get_price(5000)}원 입니다.")

# 지역변수 (매개변수도 지역변수)
def oneUp():
    x = 0
    x += 1
    return x


print(oneUp())
'''
'''
# 유효범위
quantity = 10


def price_sum(price):
    quantity = 7
    return price * quantity


print(price_sum(2000))
'''
'''
x = 0


def oneUp():
    global x
    x += 1
    return x


print(oneUp())
print(oneUp())
print(oneUp())
'''
'''
# 기본 매개변수


def pr_str(txt='안녕하세요', count=1):
    for __ in range(count):
        print(txt)


pr_str()
pr_str('hello', 5)
pr_str('hi')
'''
'''
# 함수 호출키워드


def intro(name, age, city):
    print(f"이름은 {name}이고 나이는 {age}이고 사는곳은 {city}입니다.")


intro('홍길동', 23, '서울')
intro(city='서울', name='임꺽정', age=25)
intro('홍길동', city='부산', age=59)

'''
'''
# 가변 매개변수
def calc_avg(*args):
    print(args)
    total = 0
    for i in args:
        total += i
    avg = total / len(args)
    return avg


print(calc_avg(1, 2, 3, 4, 5, 6, 7, 8))
'''
'''
# **변수는 항상 끝에 위치
def text_def(a, b, *args):
    print("text :", a)
    print('b :', b)
    print("args :", args)


text_def("hi", 1, 2, 3, 4, 5)
'''
'''
def intro(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


intro(name='홍길동', age=20, city='서울', gender='남자')
'''
'''
# 내장함수
# abs(정수) - 절대값을 구하는 내장함수


def my_abs(x):
    if x < 0:
        return -x
    else:
        return x


print(my_abs(-10))
print(my_abs(5))
print(abs(-10))
'''
'''
# 거듭제곱
print(pow(3, 4))


def my_pow(x, y):
    num = 1
    for i in range(y):
        print(f"i={i}, {num*x}={num}X{x}")
        num *= x
    return num


print(my_pow(3, 4))
'''
'''
# map()
def square(x):
    return x ** 3


numbers = [2, 4, 6, 8,]
squared = list(map(square, numbers))
print(squared)
'''
'''
# filter()
def even_number(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(even_number, numbers)))
'''
'''
# 여러게 한꺼 번에 반환
def get_return():
    arr = ['사과','바나나']
    dic = {
        'name' : '홍길동'
        'age' : 20 
    }
'''
'''
# 실습 1
numbers = []
for i in range(1, 31):
    numbers.append(i)
    i += 1


def multiple(n):
    total = 0
    for num in numbers:
        if num % n == 0:
            total += 1
            print(num, end=" ")
    print()
    print(f"{n}의 배수의 개수는: {total}")
    return


n = int(input("배수를 입력하세요: "))
multiple(n)

# 실습 1-1
# list 내포


def count(num):
    lists = [i for i in range(1, 31) if i % num == 0]
    counts = len(lists)
    return lists, counts


num = 3
lists, counts = count(num)
print(f"{num}의 배수: {lists}")
print(f"{num}의 개수: {counts}")

방법 3 중첩함수를 쓰는 방법
def count(num):
    # 중첩함수 - 이 함수 내에서만 사용이 가능
    def check(x):
        return x % num == 0

    lists = list(filter(check, range(1, 31)))
    return lists, len(lists)


num = 5
lists, counts = count(num)
print(f"{num}의 배수: {lists}")
print(f"{num}의 개수: {counts}")
'''

# # 재귀함수
# def sos(i):
#     print("Help me!")
#     if i == 1:
#         return ""
#     else:
#         return sos(i-1)


# sos(10)
'''
# n! 재귀함수로 구하기
def factorial(n):
    print(f"n의 값:{n}")
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(3))
'''


# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# n = int(input("피보나치 수열로 구할 n의값은? :"))
# print(fibonacci(n))
'''
def fibonacci(n):
    if n <= 1:
        print(n, end=" ")
        return n
    else:
        print(n, end=" ")
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))
'''

# lamda 함수
# 일반 함수

'''
def add(x, y):
    return x + y


print(add(3, 4))


def add(x, y): return x + y


print(add(3, 4))
'''


def square(x): return x ** 2


print(square(4))
print((lambda x: x ** 2)(5))
