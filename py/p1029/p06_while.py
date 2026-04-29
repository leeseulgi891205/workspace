

n_list = []
i = 0
while True:
    print("[학생성적프로그램]")
    print("[1. 학생성적입력]")
    print("[2. 학생성적출력]")
    print("[3. 학생성적수정]")
    print("0. 프로그램종료")
    print("-"*20)
    no = int(input("원하는 번호를 입력하세요."))
    # no = 0비교
    if no == 0:
        break
    elif no == 1:
        print("[학생성적입력]")
        name = input("이름을 입력하세요: ")
        kor = int(input("국어 점수를 입력하세요: "))
        eng = int(input("영어 점수를 입력하세요: "))
        math = int(input("수학 점수를 입력하세요: "))
        total = kor + eng + math
        avg = total / 3
        stu_list = [name, kor]
        n_list.append(stu_list)
        i += 1

        
        
        
# 전체 출력 [['홍길동', 100], ['유관순', 90], ['이순신', 80], ['김구', 70]]

print("[학생성적프로그램]")
print("이름\t국어\t영어\t수학\t합계\t평균\t등수\t")
print("이름\t국어")
print("-"*50)
for i in range(len(n_list)): # 0,1,2,3
    print("{}\t{}".format(*n_list[i]))


# n_list = []

# n_list.append(1) # 제일 뒤에다가 추가해라
# n_list.append(2)
# n_list.append(3)
# n_list.append(0)
# n_list.append(5)
# n_list.append(2)
# n_list.append(100)
# n_list.extend([10, 20, 30])   #리스트를 추가할 때 사용
# n_list.append([100, 200, 300])
# n_list.append(['홍길동', 100])
# print(n_list)

