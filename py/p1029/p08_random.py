import random

# 1~100사이의 숫자를 랜덤으로 출력하시오.
a_list = [] # 저장할 공간
r_num = random.randrange(1, 101)
for i in range(10):
    my_num = int(input("숫자를 입력하세요: "))
    a_list.append(my_num) # 리스트 추가
    if my_num == r_num:
        print("당첨되었습니다.")
        break
    elif r_num > my_num:
        print("더 큰 수를 입력하세요.")
    else:
        print("더 작은 수를 입력하세요.")
print("당첨번호는 {} 입니다. 축하합니다!".format(r_num))
print("입력한 번호: ", a_list)



# # randrange() 1~10까지 랜덤숫자를 3개 출력하시오.
# print(random.randrange(1,11))
# print(random.randrange(1,11))
# print(random.randrange(1,11))
# print(random.sample([1,2,3,4,5,6,7,8,9,10], k=5))
# print(random.sample(range(1,11), k=5))
# print(list(range(1,11)))