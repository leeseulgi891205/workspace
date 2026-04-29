# 조건문 if (조건
# a = 100
# if a<10: #true, false 2가지 bool(불)
#     print("참 입니다.")
    
# a = 100
# if a>10:
#     print("참 입니다.")
# else:
#     print("거짓입니다.")
    
# num = int(input("숫자를 입력하세요.>>"))  # 문자열 -> 정수타입
# if num>=0:  # 숫자와 비교
#     print("양수입니다.")
# else:
#     print("음수입니다.")

# 입력한 숫자에 50을 더 해서 100보다 큰수인지 출력하시오.
# 100보다 큰수입니다.
# 100보다 작은수입니다.

num = int(input("숫자를 입력하세요."))
num = num + 50

if num>=100:
    print("입력한 값 : " num-50, "현재값 : ",num,"100보다 큰수입니다."))
    print("입력한 값" %d, 현재갑 : &d, %s" % (num-50,num,"100보다 큰수입니다."))
else:
    print("입력한 값 : ",num-50, "현재값 : ",num,"100보다 작은수입니다.")
    print("입력한 값 : " %d, 현재갑 : &d, %s" (num-50,num,"100보다 큰수입니다."))
    
# 입력한 값이 짝수인지 홀수인지 출력하시오.
num = int(input("숫자를 입력하세요."))

if num % 2 == 0:
    print("입력한 값 : %d, 짝수입니다." % num)
else:
    print("입력한 값 : %d, 홀수입니다." % num)
    


# 문자열 연산자
# 문자열 슬라이싱

str1 = "안녕하세요"

# 안(0) 녕(1) 하(2) 세(3) 요(4)
print(srt1[0])
print(srt1[1])
print(srt1[2])
print(srt1[3])
print(srt1[4])

# 안(-5) 녕(-4) 하(-3) 세(-2) 요(-1)
print(srt1[-1])
print(srt1[-2])
print(srt1[-3])
print(srt1[-4])
print(srt1[-5])

# 1 부터 3 번 앞(2번까지)    안녕하세요
print(str1[1:3]) # 녕하
print(str1[1:4]) # 녕하세

# 입력이 없으면 끝까지
print(str1[1:]) # 녕하세요

# 처음입력값이 없으면 첫시작부터
print(str[:3])
print(str[:]) # 전부출력

# [처음번호:끝번호:스탭(증가)]
print(str1[::1]) # 안녕하세요
print([::-1]) # 요세하녕안
print(str1[1:5:2]) # 안녕하세요 -> 녕요 (2칸 띄워라)

a = "123456789"
print(a[::2])
print(a[1::2])
# 3의 배수 출력하시오.
print(a[2::3])

## 입력을 받아 마지막 글자를 출력하시오.
input1 = input("문자를 입력하시오")
print("마지막 글자 :",input[-1])

## 입력을 받아 마지막 글자를 출력하시오.
input1 = input("문자를 입력하시오")
print("마지막 글자 :",input[-1])