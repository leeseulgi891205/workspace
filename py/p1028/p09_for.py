###
bank = [1,'홍길동', 100000]
# 1번 홍길동 100,000원으로 출력 format() 함수를 사용해서

print("{}번 {}, {:,d}원".format(bank[0], bank[1], bank[2]))

name = "유관순"
rank = 3
result = 98.234567

## 이름: 유관순, 단계: 3, 성공률: 98.23% 을 format() 함수를 사용

print("이름:{}, 단계:{}, 성공률:{:.2f}".format(name,rank,result))

## f 함수
print(f"이름: {name},단계: {rank}, 성공률: {result:.2f}%")






# # for 변수 in 범위:
# for i in range(5): #[0,1,2,3,4] 0~4 5번실행
#     print(i)
    
# for i in range(5): #[0,1,2,3,4] 0~4 5번실행
#     print(i,end=" ")

# 1~100까지 합을 구하시오
# # sum = 0
# # for i in range(1,101):
# #     sum = sum + i
# # print("합계: ", sum)

# # 10을 넘는 위치는 얼마를 더할때 일까요?
# # 1+2+3+4+5+6+7+8+9+10+11+12+13+14
# # sum = 0
# # for i in range(1,101):
# #     sum = sum + i
# #     if sum > 100:
# #         break
# #     print(i,sum)
# # print(f"{i-1}  번째 , {sum-i}")


# # 1*2*3*4*5*6*7*8*9*10 결과값을 출력하시오.
# # result = 1

# result = 1
# for i in range(1, 11):
#     result = result * i
# print("결과값:", result)

# result = 1
# for i in range(1, 11):
#     result = result * i
#     if result > 100:
#         print(f"{i} 번째: {result}")
#         break
    
    

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
