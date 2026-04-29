# fruits = ['사과','배','복숭아','포도','딸기']
# print("[과일 리스트]")
# for fruit in enumerate(fruits): #enumerate() -함수 : 인덱스 번호 리턴
#     print(fruit)
#     print("{}.{}".format(i+1,fruit)) # 1.사과 2.배 .3복숭아
    
fruits = ['사과','배','복숭아','포도','딸기']
print("[과일리스트 ]")    
for i in range(5):
    print("{}.{}".format(i+1, fruits[i]))
    
fruits = ['사과','배','복숭아','포도','딸기']
print("[과일리스트]")
for i in range(len(fruits)):
    print("{}.{}".format(i+1, fruits[i]), end=" ")
print()



# 10을 넘는 위치는 얼마를 더할때 일까요?
# 1+2+3+4+5+6+7+8+9+10+11+12+13+14
sum = 0
for i in range(1, 15):
    sum += i
    print("번호: ", sum)
    if sum > 10:
        print(f"{i} 번째: {sum}")
        break
    print("합계: ", sum)
    print("10을 넘는 위치: ", i)
    
    

# 501번 부터 1000까지 홀수의 합을 출력하시오.
# sum = 0
# for i in range(501, 1001):
#     if i % 2 == 1:
#         continue
#     for j in range(501, 1001):
#         print(i,"*")
        
    
# sum = 0
# for i in range(3, 101, 3):
#     sum += i
# for i in range(501,1001):
#     if i % 2 == 1:
#         sum = sum + i
# print("합계: ", sum)

# # 1~100까지 3의 배수의 합을 출력하시오.

# sum = 0
# for i in range(1,101):
#     sum += i
    
# for i in range(1,101):
#     if i % 3 == 0:
#         sum = sum + i
# print("합계: ", sum)

        








# # for문을 2번 사용 - 중첩for문

# for i in range(2, 10):
#     print("[{}단]".format(i))
#     if i%2 != 0:
#         continue #1번만 제외(9번을 실행), break는 완전중지
#     for j in range(1, 10):
#       #print(i,"*",j,"=",i*j)
#       print("{} X {} = {}".format(i, j, i * j),end= " ")
# print()


#2중 for문을 사용해서 00,01,02,03....11,12,13....99까지 출력

# for i in range(0, 10):
#     for j in range(0, 10):
#         print(f"{i}{j}", end=" ")
#     print()
    
    
# for i in range(0, 10):
#     for j in range(0, 10):
#         for k in range(0, 10):
#             print("KB국민은행 번호표: {}{}{}".format(i,j,k))








# 이름, 국어, 영어, 수학점수를 입력받아
# 홍길동, 국어,영어,수학,합계,평균값을 fomat으로 출력하시오.
# 합계 = 국어 + 영어 + 수학

name = input("이름을 입력하세요: ")
kor = int(input("국어점수를 입력하세요: "))
eng = int(input("영어점수를 입력하세요: "))
math = int(input("수학점수를 입력하세요: "))

sum = kor + eng + math
avg = sum / 3

print("{}, {}, {}, {}, {}, {}".format(name, kor, eng, math, sum, avg))