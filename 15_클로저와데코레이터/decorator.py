# decorator.py

import time

def myfunc() :
    start = time.time()
    print("함수가 실행됩니다.")
    end = time.time()
    print("함수 수행시간 : %f 초" %(end-start))

myfunc()