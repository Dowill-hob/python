'''
# 클래스 메서드
class Converter:
    conversion_rate = 1.60934

    @classmethod
    def miles_to_kilometer(cls, mile):
        return mile * cls.conversion_rate


print(Converter.miles_to_kilometer(7))
'''
'''
# 클래스 메서드 2


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name, age)


# 클래스 메서드를 통해서 객체 생성
p1 = Person.from_birth_year("홍길동", 1990)
print(p1.name, p1.age)
'''
'''
# 클래스 메소드
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

Counter.increment()
Counter.increment()
print(Counter.get_count())
'''
'''
# 자식클래스의 정보유지


class Animal:
    species = "동물"

    @classmethod
    def get_species(cls):
        return cls.species


class Dog(Animal):
    species = "진돗개"


print(Animal.get_species())
print(Dog.get_species()) # 서브클래스의 정보를 유지시켜준다.

'''
'''
# 정적메서드


class Mathutils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b


print(Mathutils.add(30, 20))
print(Mathutils.minus(10, 20))
'''


# 날짜별 전력사용량




from abc import ABC, abstractmethod
class ElectricityData(ABC):

    def __init__(self, usage_data):
        self.usage_data = usage_data
        self.total_usage = self.calculate_total_usage()

    @abstractmethod
    def calculate_total_usage(self):
        pass

    @abstractmethod
    def get_usage_on_date(self, date):
        pass

    @property
    def usage_data(self):
        return self.usage_data

    @usage_data.setter
    def usage_data(self, value):
        self.usage_data = value

    @property
    def total_usage(self):
        return self.total_usage

    @total_usage.setter
    def total_usage(self, value):
        self.total_usage = value

    def add_usage(self, date, usage):
        self.usage_data.append({"date": date, "usage": usage})
        self.total_usage = self.calculate_total_usage()

    def remove_usage(self, date):
        for index, record in record(self.usage_data):
            if record["date"] == date:
                del self.usage_data[index]
            break
        self.total_usage = self.calculate_total_usage()


class HomeElectricityData(ElectricityData):

    def calculate_total_usage(self):
        return sum(record["usage"] for record in self.usage_data)

    def get_usage_on_date(self, date):
        for record in self.usage_data:
            if record["date"] == date:
                return record["usage"]
        return

    @classmethod
    def filter_date_range(cls, usage_data, start_date, end_date):
        return [record for record in usage_data if start_date <= entry["date"] <= end_date]

    @staticmethod
    def find_highest_usage(usage_data):
        if not usage_data:
            return
        return max(usage_data, key=lambda record: record["usage"])


electricity_usage = [
    {"date": "2024-11-01", "usage": 12.5},
    {"date": "2024-11-02", "usage": 15.3},
    {"date": "2024-11-03", "usage": 10.8},
    {"date": "2024-11-04", "usage": 14.2},
    {"date": "2024-11-05", "usage": 13.6}
]
e1 = HomeElectricityData(electricity_usage)
print(e1.usage_data)
