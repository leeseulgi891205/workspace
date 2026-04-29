#######################수정##########################


stu_list = [
    ['홍길동', 80, 90, 80, 250, 83.33],
    ['유관순', 90, 90, 90, 250, 83.33],
    ['이순신', 100, 100, 100, 300, 100.00]
    ]


titles = ['이름','국어','영어','수학','합계','평균',]

while True:

    print("[학생성적수정]")
    print("[0. 홍길동]")
    print("[1. 유관순]")
    print("[2. 이순신]")
    print("-"*30)
    # 수정할 대상 변경
    num = int(input("수정하려는 학생 번호를 입력하세요."))
    print("{} 학생을 선택하였습니다.".format(stu_list[num]))
    print("1. 국어성적수정")
    print("2. 영어성적수정")
    print("3. 수학성적수정")
    print("-"*30)
    subject = int(input("수정할 과목을 선택하세요."))

    print("[{} 학생 {} 점수를 수정".format(stu_list[num][0],titles[subject]))
    print("현재 {} 점수: ".format(titles[subject],stu_list[num][subject]))
    # 국어점수입력
    score = int(input("수정할 {} 점수를 입력하세요.".format(titles[subject],stu_list[num][subject])))
    stu_list[num][subject] = score # 국어점수변경 # 학생 영어 수학 국어 성적 바꿈
    stu_list[num][4] = stu_list[num][1]+stu_list[num][2]+stu_list[num][3] # 합계
    stu_list[num][5]+stu_list[num][4]/3 # 평균
    print(stu_list)























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