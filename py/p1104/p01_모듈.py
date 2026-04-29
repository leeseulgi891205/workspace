# 모듈 : 함수의 집합
# 다른 파일의 모듈을 사용하려면, import을 해야 사용가능
# import 를 하면 모듈이름.함수명으로 호출해야 함.

# import Func  # Func.py 모든 함수를 가져옴.
# import random

# # import 모듈이름.함수명으로 사용
# print(Func.func1())
# random.sample()

# from 파일명 import 함수를 정의하면 파일명을 생략가능
# 모듈명 생략가능
# from 모듈명 import 변수,함수,클래스
# 유사한 함수 그룹에 묶어두면 사용하기 편함.
# from Func import *
# print(func1())
# func2()    # 함수사용
# s1 = stu() # 클래스사용



# 예제
# 수학공식
# from math import sin,cos,tan,floor,ceil
# # floor 소수점 버림, ceil 소수점 올림, round 반올림
# print(floor(1.95))
# print(ceil(1.2))
# print(round(1.59))  # round 내장함수

# 모듈이름이 너무 길때 줄여 사용가능 : as 별칭
# import random as r
# import math
# print(r.randint(1,6))

# #dir : 모듈안에 모든 함수를 보여주는 명령어
# print(dir(math))  # math안에 있는 모든 함수를 보여줌
# print(dir(r))     # random안에 있는 모든 함수를 보여줌.

# 날짜와 시간을 가져오는 모듈
# 파이썬 - 날짜, html - 날짜, 자바스크립트 - 날짜, db - 날짜
# import datetime
# now = datetime.datetime.now()
# print(now)
# print(now.year) # year,month,day,hour,minute,second

# import time
# print("a")
# time.sleep(5) # 5초동안 대기
# print("b")


# 패키지 : 모듈파일을 모아둔 폴더
# from Func import func1
# from 폴더명.모듈명 import 변수,함수,클래스, *
# from 폴더명 import 모듈명

# from cal.Func import *
# from cal import Func
# print(Func.func1())