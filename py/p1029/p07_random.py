import random      # 선언, random 클래스 가져와서 쓰겠다.
print(random.random())        #0.000000000000 <= x < 1.000000000000
print(random.randrange(1,11))   # 1,10 사의의 숫자를 랜덤으로 가져옴.

# 1~10사이의 숫자를 랜덤으로 가져옴. 위에와 둘다 같음
print(random.randint(1,11))       

# 리스트에서 숫자를 랜덤으로 뽑아옴. (단 중복 불가)
print(random.sample([1,2,3,4,5,], 4))    

# 리스트에서 숫자를 랜덤으로 뽑아옴. (단 중복 가능)
print(random.choices([1,2,3,4,5], 4))    

# 리스트의 순서를 랜덤으로 섞음.
a_list = [1,2,3,4,5]
random.shuffle(a_list)



# user_nums = []
# for i in range(6):
#     num = int(input("1~45사이의 숫자를 입력하세요: "))
#     user_nums.append(num)

mport random

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


# if count == 2:
#     print("5천원")
# elif count == 3:
#     print("5만원")
# elif count == 4:
#     print("5백만원")
# elif count == 5:
#     print("5천만원")
# elif count == 6:
#     print("20억")
    

lotto = random.sample(range(1,46), 6)
# print("로또번호 [1등 당첨 되세요!]: ", lotto)


# # 6개의 숫자를 입력받아 출력하시오.

# my_list = []
# count = 0
# c_list = []
# for i in range(7):
#     my_list = int(input("숫자를 입력하세요: "))
#     my_list.append(num)
# my_list.sort()
# print(lotto)
# print("[결과화면]")
# print("-"*50)
# print(lotto)
# print(my_list)



# # lotto - [5,9,24,36,44,45]
# # my_list - [3,11,15,24,30,36]

# for i in lotto:
#     for j in my_list:
#         if i == j:
#             count = count + 1
#             c_list.append(i)
#             break
# print("당첨번호: ",c_list)
# print("정답갯수: ",count)