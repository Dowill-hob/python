'''
# 상속
# 부모클래스가 생성자가 없을때
class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

    def move(self):
        print("동물이 움직입니다.")

# 자식 클래스


class Cat(Animal):
    def meow(self):
        print("야옹!")


cat = Cat()
cat.speak()
cat.move()
cat.meow()
'''
# 부모클래스의 생성자가 존재할 때

'''
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}가 소리를 냅니다.")

    def move(self):
        print(f"{self.name}가 움직입니다.")

# 자식클래스


class Cat(Animal):
    def __init__(self, name, sound="야옹"):
        super().__init__(name)
        self.sound = sound

    def meow(self):
        print(f"{self.name}가 {self.sound}하고 울었습니다.")


cat = Cat("장화")
cat.speak()
cat.move()
cat.meow()
'''
'''
# 다중 상속


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower


class Wheels:
    def __init__(self, count):
        self.count = count


class Car(Engine, Wheels):
    def __init__(self, horsepower, count):
        Engine.__init__(self, horsepower)
        Wheels.__init__(self, count)

    def info(self):
        print(f"이 자동차는 {self.horsepower} 마력과 {self.count}개의 바퀴를 가지고있다.")


car = Car(100, 4)
car.info()
print(Car.mro())

'''
# 오버라이딩

'''
class Parent:
    def greet(self):
        print("안녕하세요. 부모 클래스")


class Child(Parent):
    def greet(self):
        print("안녕하세요. 자식 클래스")


p = Parent()
c = Child()
p.greet()
c.greet()
'''


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # 재고 업데이트 메서드
    def update_quantity(self, amount):
        self.quantity += amount
        print(
            f"{self.name} 재고가 {amount}만큼 {'증가' if amount > 0 else '감소'}했습니다. 현재 재고: {self.quantity}")

    # 상품 정보 출력 메서드
    def display_info(self):
        print(f"상품명: {self.name}")
        print(f"가격: {self.price}원")
        print(f"재고: {self.quantity}개")


class Electronic(Product):
    def __init__(self, name, price, quantity, warranty_period=12):
        super().__init__(name, price, quantity)
        self.warranty_period = warranty_period

    def extend_warranty(self, month):
        total_warranty = self.warranty_period + month
        print(
            f"보증 기간이 {self.warranty_period}개월 연장되었습니다. 현재 보증 기간: {total_warranty}")

    def display_info(self):
        super().display_info()
        print(f"보증 기간: {self.warranty_period}")


class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    def is_expired(self, current_date):
        if current_date > self.expiration_date:
            print(f"{self.name}은 유통기한이 지났습니다. ")
        else:
            print(f"{self.name}은 유통기한이 지나지 않았습니다.")

    def display_info(self):
        super().display_info()
        print(f"유통기한 : {self.expiration_date}")


e1 = Electronic("스마트TV", 150000, 5, 24)
e1.display_info()
e1.extend_warranty(12)

f1 = Food("사과", 3000, 50, "2023-12-29")
f1.display_info()
f1.is_expired("2024-11-28")

'''

# 추상화
# 추상화 클래스




from abc import ABC, abstractmethod
class PaymentSystem(ABC):

    # 추상메서드
    @abstractmethod
    def authnticate(self):  # 추상 메서드는 선언은 하되 내용을 입력하지 않는다
        pass

    @abstractmethod
    def process_payment(self, amount):
        pass

    def payment_info(self, amount):
        print(f"{amount}원 결제가 완료되었습니다.")


class kakaoPay(PaymentSystem):
    def authnticate(self):
        print("카카오페이 인증완료")

    def process_payment(self, amount):
        print(f"카카오페이로 {amount}원을 결제합니다.")


pay = 50000
kakao = kakaoPay()
kakao.authnticate()
kakao.process_payment(pay)
kakao.payment_info(pay)
'''
