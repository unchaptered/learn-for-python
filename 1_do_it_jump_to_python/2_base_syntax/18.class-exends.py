# Class extends Class

class FourCalculator:
    # 클래스 변수 선언부
    first = 10

    def __init__(self, first, second):
        # 객체 변수 선언부
        self.first = first
        self.second = second
        
    def setData(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

class MoreFourCalculator(FourCalculator):
    pass

calc_1 = MoreFourCalculator(10, 20)
calc_2 = FourCalculator(30, 40)

print(calc_1)
print(calc_2)