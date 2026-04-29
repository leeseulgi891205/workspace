import random
#1~45까지 6개의 랜덤숫자를 출력하시오. (중복불가) 가로로 출력하시오.


# lotto = random.sample(range(1,46), 6)
# print("로또번호 [1등 당첨 되세요!]: ", lotto)


# # 6개의 숫자를 입력받아 출력하시오.

# 1.번수선언
my_list = [] #입력한 번호
c_list = [] #맞춘번호 - len(c_list)
count = 0 #맞춘갯수
lotto = random.sample(range(1,46), 6) 
lotto.sort()


#결과화면 출력
for i in range(7):
    my_list = int(input("숫자를 입력하세요: "))
    my_list.append(num)
my_list.sort()
print(lotto)
print("[결과화면]")
print("-"*50)
print(lotto)
print(my_list)



# # lotto - [5,9,24,36,44,45]
# # my_list - [3,11,15,24,30,36]

for i in lotto:
    for j in my_list:
        if i == j:
            count = count + 1
            c_list.append(i)
            break
print("당첨번호: ",c_list)
print("정답갯수: ",count)

# 당첨금 출력
# 로또를 0,1 2개 맞추면 5천원 3개 맞추면 5만원 4개 맞추면 5백만원 5개 맞추면 5천만원 6개 맞추면 20억


if count == 2:
    print("5천원")
elif count == 3:
    print("5만원")
elif count == 4:
    print("5백만원")
elif count == 5:
    print("5천만원")
elif count == 6:
    print("20억")
