
# 매개변수 개수는 호출하는 변수의 개수와 일치해야한다.
# 매개변수 타입도 호출하는 변수타입과 일치해야한다.

# def add(a,b):
#     return a + b

# a = add(1,2,3)
# print(a)

# 가변 매개변수 : 매개변수의 개수가 정해져 있지 않을 때 사용.
# def add(a,b,*c): # 변수 앞에 *를 붙히면 가변 매개변수가 됨.
#    sum = a+b
#    for i in c: # c: 여러개 가능.
#        sum += i
#    return sum

# print(add(1,2,3,4,5,6,7,8,9,10))
# print(1,2,3)



#

# def print_str(a,b,*c): # 가변 매개변수는 맨 뒤에 위치해야함.
#     print(a)
#     print(b)
#     for i in c:
#         print(i)
        
# print_str("안녕","사과","홍길동","점수",100)

# 여러개를 입력받아, 함수를 사용해서 출력하시오.
# def print_str(*c):
#    for i in args:
#        print(i)

# 무한반복변수로 5번 입력받아 모두 출력하시오. 0을 입력받으면 종료.
# str1 = [0,0,0,0,0]
# for i in range(5):
#    str[i] = input("문자를 입력하세요.(종료:0)>>")
    
# print_str(*str1)

stus = [1,'홍길동',100,90,80]

# 국어, 영어, 수학 점수를 입력받아 return함수를 적용.
def sum(kor,eng,math):
    return (kor + eng + math)

def avg(kor,eng,math):
    return (kor + eng + math, (kor + eng + math)/3)



# stus = [1,'홍길동', 100,90,80]
# 함수를 제대로 구성해서 stus 리스트를 아래와 같이 변경하시오.
# stus = [1,'홍길동',100,90,80,270,90,00]으로 변경하시오.
# 함수를 꼭 사용할것.

stus.append(sum(stus[2],stus[3],stus[4]))
stus.append(sum)
print(stus)

stus.append(avg(stus[2],stus[3],stus[4]))
stus.append(avg)
print(stus)


def cal(a,b):
    sum = 0
    for i in range(a,b+1):
        sum += i
    print(sum)
cal(1,10)