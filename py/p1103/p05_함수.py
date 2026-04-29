def cal(a,b):
    print("[사칙연산]")
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    
# 두수를 입력받아 사칙연산 수행. 함수를 사용할것
# 무한반복 되도록 하시오.
# 0을 입력받으면 종료.

i = 0
a_list =[0,0]
while True:
    a = input("첫번째 숫자 입력하세요.") # str
    if a.isdigit(): 
        a_list[i] = int(a) # 숫자인지 확인
        i += 1 # 1 증가
    else : print("숫자만 입력하세요.")
    if i == 2: break
cal(a_list[0],a_list[1])

while True:
    a = int(input("첫번째 숫자 입력.(종료:0)"))
    if a == 0:
        print("종료합니다.")
        break
    b = int(input("두번째 숫자 입력.(종료:0)"))
    if b == 0:
    cal(a,b)

while True:
    a = int(input("첫번째 숫자 입력(종료:0)"))
    if a == 0:
        print("종료합니다.")
        break
    b = int(input("두번째 숫자 입력(종료:0)"))
    if b == 0:
        print("종료합니다.")
        break
    cal(a,b)


    









# def kor_hello(a):
#     print("[반복횟수]")
#     for i in range(a):
#         print("안녕하세요.")
        
# kor_hello(10)
# kor_hello(7)
# kor_hello(5)

