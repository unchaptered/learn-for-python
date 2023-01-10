# Exception Handler

try:
    # 오류가 발생할 수 있는 구문
    print('OIOI')
except Exception as e:
    # 오류 발생
    print('EXCEPTION IS OCCURED', e)
else:
    # 오류가 발생하지 않음
    print('EXCEPTION IS NOT OCCURED')
finally:
    # 무조건 마지막에 1회 실행
    print('FINISHED')