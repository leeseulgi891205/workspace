stu_list = [
    [10101, '홍길동', 80, 90, 80, 250, 83.33],    # 첫 번째 학생 정보
    [10102, '유관순', 90, 90, 90, 270, 90.00],    # 두 번째 학생 정보
    [10103, '이순신', 100, 100, 100, 300, 100.00] # 세 번째 학생 정보
]

stu_count =10104 # 학생번호
titles = ['번호', '이름', '국어', '영어', '수학', '합계', '평균']

def stu_print():
    global stu_count # 전역변수
    print("-"*50)
    print("학생성적관리프로그램")
    print("-"*50)
    print("-"*30)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("0. 프로그램종료")
    print("-"*30)


def stu_input():
    # 단순변수가 선언되면 함수에서는 변수를 새롭게 생성
    global stu_count # 전역변수
    print("[학생성적입력]")
    name = input(f"{stu_count} 번 학생의 이름을 입력하세요.")
    kor = int(input("국어 점수를 입력하세요."))
    eng = int(input("영어 점수를 입력하세요."))
    math = int(input("수학 점수를 입력하세요."))
    print("점수에는 숫자만 입력하세요.")  
total = kor + eng + math
avg = total / 3
stu_list.append([stu_count, name, kor, eng, math, total, avg])
stu_count += 1
print("성적 입력이 완료 되었습니다.\t")

# 학생성적 프로그램
    while True:
        stu_print()  # 함수호출
        choice = int(input("원하는 번호를 입력하세요."))
        if choice == 1:   # 학생성적 입력부분
            stu_input()
        elif choice == 2:  # 학생성적 출력부분
            stu_print()
            pass

def stu_print():
    print(" "*10,"[학생성적리스트]")
    print("-"*50)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*titles))
    for student in stu_list:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*student))