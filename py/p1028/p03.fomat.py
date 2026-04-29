# year = 2025
# month = 10
# day = 28
# # 2025년 10월 28일 출력
# print("%d년 %d월 %d일" % (year,month,day))

# #포맷함수 format()
# date1 = "{}년 {}월 {}}일".format(year,month,day)
# print(date1)

#포맷함수는 저장
# a = 10000000
# a_format = "{}".format(a)
# a_format1 = "{:10d}".format(a)
# a_format2 = "{:010,d}".format(a) #,를 넣으면 1000단위 표시
# print(a_format)
# print(a_format1)
# print(a_format2)

# b = 25.2345678
# b_format = "{}".format(b)
# b_format1 = "{:.2f}".format(b)
# print(b_format)
# print("{:.2f}".format(b))


# list타입 format함수 사용
# stus = ['홍길동',100,90,80]
# print("이름: {},국어: {},수학: {}".format(\
#     stus[0],stus[1],stus[2],stus[3],)
# # *stus -> 전개연산자 stus[0],stus[1],stus[2],stus[3]
# print("이름:{},국어:{},영어{},수학{}".format(*stus))



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




# % print
# a = 10
# print("%d" % a)
# print("%5d" % a)
# print("%5d" % a)
# print("%05d" % a) # 빈공간의 0

# b = 10.2345678
# print("%f" % b)
# print("%.2f" % b)
# print("%7.2f" % b)
# print("%07.2f" % b)
