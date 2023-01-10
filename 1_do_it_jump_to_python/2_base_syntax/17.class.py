# Class

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

cal_1 = Calculator()
cal_2 = Calculator()
print('cal_1.result', cal_1.result) # cal_1.result 0
print('cal_2.result', cal_2.result) # cal_2.result 0

cal_1.add(10)
cal_2.add(200)
print('cal_1.result', cal_1.result) # cal_1.result 10
print('cal_2.result', cal_2.result) # cal_2.result 200

# Class 2
# instance_name.setData(10, 20)
# instance_name이 self안에 들어간다고 생각하면, 10이 first 20이 second이다.

class FourCalculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
    def setData(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

cal_3 = FourCalculator()
cal_3.setData(30, 100)
print(cal_3.first, cal_3.second)    # 30 100
print(cal_3.add())                  # 130
