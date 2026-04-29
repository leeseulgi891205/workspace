stu_list = [
    ['홍길동', 80, 90, 80, 250, 83.33],
    ['유관순', 90, 90, 90, 250, 83.33],
    ['이순신', 100, 100, 100, 300, 100.00]
    ]

titles = ['이름','국어','영어','수학','합계','평균',]

# 0. 홍길동
# 1.유관순
# 2. 이순신
# stu_list를 가지고 이름을 출력 하시오.

while True:
    print("[ 학생성적삭제 리스트 ]")
    for idx,stus in enumerate (stu_list):
            print("{}\t{}\t".format(idx+1,*stus))
    print("-"*50)
    num = int(input("삭제할 번호를 입력하세요.")) # 1 -> 0
    del stu_list[num-1]  # 리스트 삭제 방법
    print(stu_list)

    # # 리스트 삭제 방법
    # a_list = [1,2,3]
    # del a_list[0]  # 인덱스 0번 삭제
    
    