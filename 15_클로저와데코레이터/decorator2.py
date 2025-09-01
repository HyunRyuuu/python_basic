# decorator.py

import time

def elapesd(original_func) : # 함수를 인수로 받음
    def wrapper() :
        start = time.time()
        result = original_func() # 함수를 수행
        end = time.time()
        print("함수 수행시간 : %f 초" %(end-start)) # 함수의 수행시간을 출력
        return result # 함수의 수행 결과를 반환
    return wrapper

def myfunc() :
    print("함수가 실행됩니다.")

decorated_myfunc = elapesd(myfunc)
decorated_myfunc()