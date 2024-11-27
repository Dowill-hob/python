'''
# 클래스

# 클래스 정의
class Car:
    model = ""
    cc = 0

    # 함수 추가
    def info(self):  # self keward가 아님 아무 단어나 있어도 됨 하지만 self가 관례
        print(f"모델명: {self.model}, 배기량: {self.cc} cc")


# 사용
car1 = Car()  # 인스턴스 생성
car1.model = "싼타페"
car1.cc = 2000
car1.info()
'''
'''
# 생성자 존재할때


class Car:

    def __init__(self, model, cc):
        self.model = model
        self.cc = cc

    def __str__(self):
        return f"모델명: {self.model}, 배기량: {self.cc} cc"

    def get_info(self):
        print(f"모델명: {self.model}, 배기량: {self.cc} cc")


car1 = Car("싼타페", 2000)
car2 = Car("BMW", 2200)
# car1.get_info()
# car2.get_info()
print(car1)
print(car2)
print("====== 승용차 리스트 ======")
cars = [
    Car("소나타", 2000),
    Car("쏘렌토", 3000),
    Car("아반떼", 1600)
]
for car in cars:
    print(car)
'''
'''

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return f"두 수의 합:{self.num1 + self.num2}"

    def sub(self):
        if self.num1 >= self.num2:
            return f"두 수의 차:{self.num1 - self.num2}"
        return f"두 수의 차:{self.num2 - self.num1}"

    def mul(self):
        return f"두 수의 곱:{self.num1 * self.num2}"

    def div(self):
        if self.num2 == 0:
            return "분모는 0일 될수 없습니다."
        return f"두 수의 나눔:{self.num1 / self.num2}"


number1 = Calculator(4, 5)

print(number1.add())
print(number1.sub())
print(number1.mul())
print(number1.div())
'''
'''
# 클래스변수와 인스턴스 변수


class Dog:
    kind = "진돗개"  # 클래스변수

    def __init__(self, name):
        self.name = name  # 인스턴스 변수


# 인스턴스변수 접근
dog1 = Dog("백구")
dog2 = Dog("초코")

print(dog1.name)
print(dog2.name)

# 클래스변수 접근
# print(dog1.kind) # 사용안함
# print(dog2.kind) # 사용안함

print(Dog.kind)
'''

'''
class Example:
    shared = "공유 변수"  # 클래스변수

    def __init__(self, name):
        self.name = name  # 인스턴스 변수

# 인스턴스 변수는 공유되지 않음
e1 = Example("A")
e2 = Example("B")
Example.shared = "변경된 공유 변수"
print(e1.shared)
print(e2.shared)
e1.name = "C"
print(e1.name)
print(e2.name)
'''
'''
# 사번 자동 발급


class Employee:
    serial_num = 1000  # 클래스 변수

    # def __init__(self, name):
    #     Employee.serial_num += 1
    #     self.id = Employee.serial_num
    #     self.name = name

    def __init__(self, name):
        self.serial_num = 1000
        self.serial_num += 1
        self.id = self.serial_num
        self.name = name

    def __str__(self):
        return f"사번 : {self.id}, 이름 : {self.name}"


e1 = Employee("홍길동")
print(e1)
e2 = Employee("임꺽정")
print(e2)
employees = [Employee("이몽룡"), Employee(
    "심청이"), Employee("변사또"), Employee("전우치")]
for employee in employees:
    print(employee)
'''

'''
class Supermaket:

    # total_customer = 0
    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer

    def print_location(self):
        return f"위치: {self.location}"

    def change_category(self, new_product):
        self.product = new_product

    def show_list(self):
        return f"상품: {self.product}"

    def enter_customer(self):
        self.customer += 1
        #supermarket.custoker += 1 # 모든 가게 손님 수의 합
    def show_info(self):
        return f"위치: {self.location}, 이름: {self.name}, 상품: {self.product}, 고객 수: {self.customer}"


market1 = Supermaket("마포구 염리동", "마켓온", "음료", 12)
market1.enter_customer()
print(market1.print_location())
print(market1.show_list())
print(market1.show_info())
market1.change_category("과자")
print(market1.show_list())
'''

# 정보은닉


class Person:
    def __init__(self):
        self._name = " "
        self._age = 0

    # 이름을 설정
    def setname(self, name):
        self._name = name

    # 이름을 출력
    def getname(self):
        return self._name

    # 나이를 설정
    def setage(self, age):
        self._age = age

    # 나이를 출력
    def getage(self):
        return self._age


p1 = Person()
p1.setname("아무개")
print(p1.getname())
p1.setage(20)
print(p1.getage())
