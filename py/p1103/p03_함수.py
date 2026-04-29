# 함수: 특정명령어를 집합 - 반복을 제거, 유지보수를 쉽게 하기 위해 사용 - 코드량도 대폭 줄일수 있음.
# 함수 : 덧셈, 뺄셈, 곱셈, 나눗셈을 수행하는 함수를 각각 정의하고,
# 두 개의 숫자를 입력받아 각 함수를 호출하여 결과를 출력하는 프로그램을 작성하시오.

# 함수형태
# def 함수명():
#     pass

# 함수 호출
# 함수명()

def calculate(a,b): # 함수 정의 #매개변수
    print("더하기",a+b)
    print("빼기",a-b)
    print("곱하기",a*b)
    print("나누기",a/b)
    
a,b = 10,2
calculate(10,2)
a,b = 5,3
calculate(a,b)
a,b = 2,1 
calculate(a,b) # 함수 호출



# a,b = 10,2
# print("더하기:",a+b)
# print("빼기:",a+b)
# print("곱하기:",a+b)
# print("더하기:",a+b)
# print("나누기:",a/b)

# a,b = 5,3
# print("더하기:",a+b)
# print("빼기:",a+b)
# print("곱하기:",a+b)
# print("더하기:",a+b)
# print("나누기:",a/b)


