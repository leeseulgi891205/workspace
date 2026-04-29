# 함수사용목적 - 반복제거, 유지보수 편의성, 코드관리의 편의성.



# def cal()
# 1~10까지 합이 출력되도록 구성하시오.


def cal():
    sum = 0
    for i in range(num1,num2+1):
        sum += i
    print("합계: ",sum)

# 함수호출
# 값을 출력하시오.
num1 = int(input("숫자를 입력하세요>>"))
num2 = int(input("숫자를 입력하세요>>"))
sum = 0
cal(num1,num2)

cal(2,10)
cal(5,9)
cal(11,20)
















# 함수를 사용 cal(3)
# 두수와 +=*/ 4개중에 1개를 입력받아
# 두수의 결과를 출력하시오.
# num1 = int(input("숫자를입력하세요."))
# num2 = int(input("숫자를입력하세요."))
# str1 = input("원하는 사칙연산 기호를 입력하세요.(+,-,*,/)")
# def cal(num1,num2,str1):
#     if str1 == '+':
#         return num1 + num2
#     elif str1 == '-':
#         return num1 - num2
#     elif str1 == '*':
#         return num1 - num2
#     elif str1 == '/':
#         return num1 - num2
#     else:
#         return "잘못된 숫자입니다."
# result = cal(num1,num2,str1)
# print(result)








# 입력한 글자를 입력한 숫자만큼 반복 출력하시오.
# def s_print(str1,num):
#     for i in range(num):
#         print(str1)
        
        

# str1 = input("글자를 입력하세요>>")
# num = int(input("반복 횟수를 입력하세요>>"))
# s_print(str1,num)