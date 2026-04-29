#1~5까지 for문을 사용해서 출력
#5번 입력받아서 값을 출력하시오.
# for 변수 in 범위:
# 숫자를 입력받아, 입력받은 값을 출력하는 것을 5번 반복하시오.

# for i in range(5): # for :
#     num = int(input("{}숫자를 입력하세요.".format(i+1)))
#     print("{}입력받은 숫자: {}".format(i+1,num)) # 반복해야 할내용 들여쓰기를 해야 함.
    

# 1~10까지 숫자의 합을 출력하시오. 반복 10번
# for i in range(10): # 0~9
# for i in range(1,11): # 1~10
#     sum = 0
#     sum = sum + i
#     print("합계: ", sum)

# 1~10까지 홀수 합계를 구하시오.
# range 스탭을 사용해서 할 것

sum = 0
for i in range(1,11,2): #1~10
    sum = sum + i
print("홀수 합계: ", sum)

# if 조건문을 사용해서 할 것
for i in range(1,11):
    if i % 2 == 1: 
        sum = sum + i 
print("홀수 합계: ", sum)

    




# # for문 - 
# # 구조 - for 변수 in 범위(range,list.문자열):

# for i in range(10):
#     print(i)

# # 반갑습니다. 10번출력
# for i in range(10):
#     print("반갑습니다")
    
# a_list = []
# for i in range(10):
#     num = int(input("{}숫자를 입력하세요.".format(i+1)))
#     if num % 2 == 0: # 짝수만
#         break # 반복문 종료 명령어
#     # append
#     a_list.append(num)
    
# print("리스트 :", a_list)


