# 학생입력부분
import random

stu_list = [
    [10101, '홍길동', 80, 90, 80, 250, 83.33],    # 첫 번째 학생 정보
    [10102, '유관순', 90, 90, 90, 270, 90.00],    # 두 번째 학생 정보
    [10103, '이순신', 100, 100, 100, 300, 100.00] # 세 번째 학생 정보
]

stu_count =10104

titles = ['번호', '이름', '국어', '영어', '수학', '합계', '평균']

while True:
    print("-"*50)
    print("-"*30)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("0. 프로그램종료")
    
# 학생출력부분
    try:
        choic = ine(input("원하는 번호를 입력하세요."))
    except ValueError:
        print("올바른 숫자를 입력하세요\t")
        continue
    
    
    if choic == 1:
        print("[학생성적입력]")
        name = input(f"{stu_count} 번 학생의 이름을 입력하세요.")
    
        try:
            kor = int("국어 점수를 입력하세요.")
            eng = int("국어 점수를 입력하세요.")
            matc = int("국어 점수를 입력하세요.")
        except ValueError:
            print("점수에는 숫자만 입력하세요.")
            continue
    
        total = kor + eng + matc
        avg = total / 3
        stu_list.append([stu_count, name, kor, eng, math, total, avg])
        stu_list += 1
        print("성적 입력이 완료 되었습니다.\t")
    
    elif choic ==2:
        print(" "*10,"[학생성적리스트]")
        print("-"*50)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*titles))
        print("-"*50)
        for stus in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{:.of}\t{:.2f}".format(*stus))
            
    elif choic == 3:
        print("[학생성적수정]")
        for i, stu in enumerate(stu_list):
            print(f"[{i}] {stu[1]}")
        print("-"*50)
        
        try:
            num = int(input("수정하려하는 학생 번호를 입력하세요."))
        except ValueError:
            print("올바른 숫자를 입력하세요.\t")
            continue
    
    if num <0 or num >= len(stu_list):
        print("올바른 학생 번호를 입력하세요.\t")
        continue
    
    print(f"{stu_list[num][1]}")
    print("1. 국어성적수정")
    print("2. 영어성적수정")
    print("3. 수학성적수정")
    print("-"*50)
    
    try:
        subject = int(input("수정할 과목을 선택하세요:"))
    except ValueError:
        print("")
        


