# 이름, 국어, 영어, 수학점수를 입력받아
# 홍길동, 국어,영어,수학,합계,평균 fomat으로

a_list = ['홍길동',100,90,80,270,90,00000000]
name = input("이름을 입력하세요: ")
kor = int(input("국어 점수를 입력하세요: "))
eng = int(input("영어 점수를 입력하세요: "))
math = int(input("수학 점수를 입력하세요: "))
total = kor + eng + math
avg = total / 3
result = "이름: {}, 국어: {}, 영어: {}, 수학: {}, 합계: {}, 평균: {:.2f}".format(
    name, kor, eng, math, total, avg)
print(result)
# (*a_list)

a = 10
b = 20
print("1번째값: {2:},2번째값: {0:}".format(a,b))
print(f"1번째값: {a},2번째값: {b}")






# 3개의 값을 입력받아, 숫자를 모두 합친 금액을 출력하시오.
# 금액 : 1,000,000원

# num1 = int(input("첫번째 숫자를 입력하세요: "))
# num2 = int(input("두번째 숫자를 입력하세요: "))
# num3 = int(input("세번째 숫자를 입력하세요: "))
# total = num1 + num2 + num3
# mon_format = "총 금액: {:,}원".format(total)
# print(mon_format)
# num1 = ("총 금액: {:,d} 원".format(total))




# year = 2025
# month = 10
# day = 28
# print("%d 년 %03d 월 %d 일" % (year,month,day))
# day_format = "{} 년 {:03d} 월 {} 일".format(year,month,day)
# print(day_format)