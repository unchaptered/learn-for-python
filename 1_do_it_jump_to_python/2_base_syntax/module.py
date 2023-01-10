def printHello():
    print('hello')

# 이 코드로 module.py가 직접호출될 때만 실행할 수 있게 함수화
if __name__ == '__main__':
    print(printHello())
    print(printHello())