#조건문 - if문
#반복문 - 여러번 실행
#for, while()

#문자열,리스트 슬라이싱 [시작:끝-1:스탭]
#range - 범위 , range(10)
#range(시작,끝-1,단계스탭), range(끝):0 ~ 끝 -1
#for 변수 in 범위 - 문법
for i in range(10): # 0 ~ 10-1
    print(i)

for i in range(5): #0~4
    print("안녕하세요.")
    
for _ in range(5): #0~4 5번실행
    print("hello")
    
for i in range(5): #0~4 5번실행
    print(i+1,"번째 안녕")

for i in range(1,6):#1,5까지 5번실행
    print(i+1,"번째")
    
for i in range(1,11,2):#1~10까지 10번실행
    print(i)
    
sum = 0
for i in range(1,11):
    sum = sum + i
print("{}번째: {} ".format(i,sum))
    
    
print("총합계: ", sum)


a_list = ["홍길동",100,90,80]
for a in a_list: # a_list[0],a_list[1],a_list[2],a_list[3]
    print(a)
    
#2차원 리스트 - for문 2번, 3차원리스트 for문 3번


name = "홍길동유관순이순신"
for i in name:
    print(i)
    
# range() 사용해서 숫자를 입력하세요를 10번출력


    # print("{}번째: 숫자를 입력하세요.".format(i+1))
sum = 0
for i in range(10):
    num = int(input("{}번째: 숫자를 입력하세요.".format(i+1)))
    sum += num
print("숫자의 총합계: ", sum)