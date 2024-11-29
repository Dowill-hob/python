
from abc import ABC, abstractmethod
electricity_usage = [
    {"date": "2024-11-01", "usage": 12.5},
    {"date": "2024-11-02", "usage": 15.3},
    {"date": "2024-11-03", "usage": 10.8},
    {"date": "2024-11-04", "usage": 14.2},
    {"date": "2024-11-05", "usage": 13.6}
]


class ElectricityData(ABC):

    def __init__(self, usage_data):
        self._usage_data = usage_data
        self._total_usage = self.calculate_total_usage()

    @property
    def usage_data(self):
        return self._usage_data

    @usage_data.setter
    def usage_data(self, value):
        self._usage_data = value
        self._total_usage = self.calculate_total_usage()

    @property
    def total_usage(self):
        return self._total_usage

    @total_usage.setter
    def total_usage(self, value):
        self._total_usage = value

    @abstractmethod
    def calculate_total_usage(self):
        pass

    @abstractmethod
    def get_usage_on_date(self, date):
        pass

    def add_usage(self, date, usage):
        self._usage_data.append({"date": date, "usage": usage})
        self._total_usage = self.calculate_total_usage()

    def remove_usage(self, date):
        self._usage_data = [
            data for data in self._usage_data if data["date"] != date]
        self.total_usage = self.calculate_total_usage()


class HomeElectricityData(ElectricityData):
    def __init__(usage, usage_data):
        super().__init__(usage_data)

    def calculate_total_usage(self):
        return sum(data["usage"] for data in self._usage_data)

    def get_usage_on_date(self, date):
        for data in self._usage_data:
            if data["date"] == date:
                return data["usage"]
        return

    @classmethod
    def filtered(cls, usage_data, start_date, end_date):
        filtered_data = [
            data for data in usage_data if start_date <= data["date"] <= end_date
        ]
        return filtered_data

    @staticmethod
    def find_highest_usage(usage_data):
        if not usage_data:
            return
        return max(usage_data, key=lambda x: x["usage"])


e1 = HomeElectricityData(electricity_usage)
print(f"총 전력 사용량: {e1.total_usage:.1f}")
date = "2024-11-03"
print(f"{date}의 사용량: {e1.get_usage_on_date(date)}")
e1.add_usage("2024-11-06", 16.4)
filtered_data = HomeElectricityData.filtered(
    electricity_usage, "2024-11-02", "2024-11-04")
print(f"특정 날짜 범위 내의 전력 사용량:{filtered_data}")
print(f"가장 높은 사용량:{HomeElectricityData.find_highest_usage(electricity_usage)}")
