my_list = [] #입력한 번호
c_list = [] #맞춘번호 - len(c_list)
count = 0 #맞춘갯수
lotto = random.sample(range(1,46), 6) 
lotto.sort()
for i in range(7):
    my_list = int(input("숫자를 입력하세요: "))
    my_list.append(num)
my_list.sort()
print(lotto)
print("[결과화면]")
print("-"*50)
print(lotto)
print(my_list)




a_list = [1,2,3,4,5,6,7,8,9,10]
print(a_list)
###############################################중요########################################
b_list = list(range(1,10))
print(b_list)
##############################################중요#########################################
c_list = [i for i in range(1,10)]
print(c_list)

# 리스트 자동화
b_list = ['0','0','0','0','0','0','0','0','0','0']
print(b_list)
e_list = list('0; *9')
print(e_list)
f_list = ['0' for i in range(9)]
print(f_list)


# print(a_list)
# ###############################################중요########################################
# b_list = list(range(1,10))
# print(b_list)
# ##############################################중요#########################################
# c_list = [i for i in range(1,10)]
# print(c_list)
# a_list = [1,2,3,4,5,6,7,8,9,10]

# # 리스트 자동화
# b_list = ['0','0','0','0','0','0','0','0','0','0']
# print(b_list)
# e_list = list('0; *9')
# print(e_list)
# f_list = ['0' for i in range(9)]
# print(f_list)


# a_list = list(range(1,10))
# b_list = []
# # [
#    # [ 1,2,3 ]
#     # [ 4,5,6 ]
#     # [ 7,8,9 ]
    
# # 1 2 3
# # 4 5 6
# # 7 8 9
# # print(a_list)
# for i in a_list:
#     print(i, end=' \t')
#     if i % 3 == 0:
#         print()

# 4*4 리스트형태로 출력하시오.
# [4*4 리스트 형태]
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16






import random

# 5*5 = 25
# 리스트 생성
a_list = list(range(1,26))
# 리스트 섞기
random.shuffle(a_list)
print(a_list)

while True:
    # 리스트 화면출력
    print("         [좌표맞추기 게임]")
    for idx,a in enumerate(a_list):
        print(a, end='\t')
        if(idx+1) % 5 == 0:
            print()
    print('-'*50)
    num = int(input("원하는 번호를 입력하세요."))
    print()
    
    
    # 번호비교
    for idx,a in enumerate(a_list):
         if num ==a:
             a_list[idx] = "x"
             break
         
# a_list = [1,2,3,4,5,]
# b_list = list(range(1,6))
# c_list = [i for i in range(1,6)] # 리스트 내포
# print(a_list)
# print(b_list)
# print(c_list)

# # append, insert, extend
# # pop,del,remve,clear
# # 수정: a_list[index] = 값
# # index: 해당 위치값을 리턴해서 알려줌

# aa_list = [10,5,15,7,9]
# print(aa_list.index(10))

# # 1번째 비교
# # print(a_list)
# # num = int(input("원하는 번호를 입력하세요."))
# # for idx, aa in enumerate(aa_list):
# #     if aa == num:
# #         aa_list[idx] = "x"
# # print(aa_list)


# # 2번째 비교
# print(a_list)
# num = int(input("원하는 번호를 입력하세요."))
# if num in aa_list:
#     aa_list.index(num)
#     aa_list[aa_list.index(num)] = "x"
    
# print(aa_list)











# 가로시작 0,1,2,3,4,5,6,7,8,9
# 세로시작 0,1,2,3,4,5,6,7,8,9
# 무조건 0부터 시작


# 0. 홍길동
# 1. 유관순
# 2. 이순신
# -------------------------------------------------------
# 수정하고 싶은 학생번호를 입력하세요.
# 국어점수를 변경하는 프로그램을 구현하시오.

# print('''
#         [수정할 학생번호]
#         0. 홍길동
#         1. 유관순
#         2. 이순신
#         '''
# )
# num = int(input("수정할 학생번호를 입력하세요."))
# # 1번선택
# # 국어점수를 70점으로 변경하고, 합계 , 평균변경해서 출력하시오.
# stu_list[1][1]
# print(stu_list)
# stu_list[1][1] = 70
# stu_list[1][4] =  stu_list[1][1]+stu_list[1][2]+stu_list[1][3]
# stu_list[1][5] = stu_list[1][4]/3
# print(stu_list)


# stu_list[2][2] = 70
# stu_list[2][4] =  stu_list[2][2]+stu_list[2][3]+stu_list[2][4]
# stu_list[2][5] = stu_list[2][4]/3
# print(stu_list)






# print(stu_list[1][3])
# print(stu_list[2][0])
# stu_list[2][2] = 80
# print(stu_list)





# # 2차원 배열

# a_list = [1,2,3,4,5,6,7,8,9] # len(a_list) 9
# b_list = [                     # len(b_list) 3
#     [1,2,3], #= 세로 0,1,2
#     [4,5,6,], #= 가로 0,1,2
#     [7,8,9,]
#     ]



# a_list [3] =100
# print(a_list)
# b_list [1][0] =100
# print(b_list)

# b_list[2][1]
# print(b_list)

# # for a in a list:
# #     print(a,end="\t")
# # print()

# # for b in b_list:
# #     for b in bs:
# #         print(b_list="\t")
         
         
         
stu_list = [
    ['홍길동', 80, 90, 80, 250, 83.33],
    ['유관순', 90, 90, 90, 250, 83.33],
    ['이순신', 100, 100, 100, 300, 100.00]
    ]


print("[학생성적수정]")
print("[0. 홍길동]")
print("[1. 유관순]")
print("[2. 이순신]")
print("-"*30)
# 수정할 대상 변경
num = int(input("수정하려는 학생 번호를 입력하세요."))
print("[{} 학생 국어점수를 수정".format(stu_list[num][0]))
print("현재 국어점수: ",stu_list[num][1])
# 국어점수입력
score = int(input("수정할 국어점수를 입력하세요."))
stu_list[num][2] = score # 국어점수변경 # 학생 영어 수학 국어 성적 바꿈
stu_list[num][4] = stu_list[num][1]+stu_list[num][2]+stu_list[num][3] # 합계
stu_list[num][5]+stu_list[num][4]/3 # 평균
print(stu_list)