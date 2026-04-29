import random

stu_list = [
    [10101, '홍길동', 80, 90, 80, 250, 83.33],    # 첫 번째 학생 정보
    [10102, '유관순', 90, 90, 90, 270, 90.00],    # 두 번째 학생 정보
    [10103, '이순신', 100, 100, 100, 300, 100.00] # 세 번째 학생 정보
]

stu_count =10104

titles = ['번호', '이름', '국어', '영어', '수학', '합계', '평균']

# 프로그램 시작
while True:
    print("-"*50)
    print("-"*5, "[학생성적프로그램]")
    print(""*50)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("0. 프로그램종료")
    print(""*50)
    
    try:
        choice = int(input("원하는 번호를 선택하세요: "))
    except ValueError:
        print("올바른 숫자를 입력하세요.\t")
        continue

# 1. 학생 성적 입력.

    if choice == 1:
        print("[학생성적입력]")
        name = input(f"{stu_count}번 학생 이름을 입력하세요:")
        
        
        try:
            kor = int(input("국어 점수를 입력하세요: ")) 
            eng = int(input("영어 점수를 입력하세요: "))    
            math = int(input("수학 점수를 입력하세요: "))   
        except ValueError: 
            print("점수는 숫자만 입력하세요.\n")
            continue
            
        total = kor + eng + math  
        avg = total / 3           
        
        stu_list.append([stu_count, name, kor, eng, math, total, avg])
        stu_count += 1 
        print("성적 입력이 완료되었습니다.\n")
        
# 2. 학생 성적 출력

    elif choice == 2:
        print(" "*10,"[학생성적리스트]")
        print(" "*50)
        print("{} \t{} \t{} \t{} \t{} \t{} \t{}".format(*titles))
        print("-"*50)
        for stus in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{:.0f}\t{:.2f}".format(*stus))
        print("-"*50)
    
# 3. 학생 성적 수정

    elif choice == 3:
        print("[학생성적수정]")
        for i, stu in enumerate(stu_list):
            print(f"[{i}] {stu[1]}")
        print("-"*50)
        
        try:
            num = int(input("수정하려는 학생 번호를 입력하세요:"))
        except ValueError:
            print("올바른 숫자를 입력하세요.\t")
            continue
        
        if num < 0 or num >= len(stu_list):
            print("올바른 학생 번호를 입력하세요.\t")
            continue
        
        print(f"{stu_list[num][1]} 학생을 선택하였습니다.")
        print("1. 국어성적수정")
        print("2. 영어성적수정")
        print("3. 수학성적수정")
        print("-"*50)
        
        try:
            subject = int(input("수정할 과목을 선택하세요."))
        except ValueError:
            print("올바른 숫자가 아닙니다.")
            continue
        
        if subject < 1 or subject > 3:
            print("1, 2, 3 중에서 선택하세요.\t")
            continue
        
        print(f"[{sut_list[num[1]]} 학생 {titles[stu_list]}]")
        print(f"현재 {titles[subject+1]} 점수: {stu_list}")
        
        try:
            score = int(input(f"수정할 {titles}{[subject+1]}"))
        except ValueError:
            print("점수는 숫자만 입력하세요.\t")
            continue
        
        stu_list[num][subject+1] = score
        stu_list[num][5] = stu_list[num][2] + stu_list[num][3] + stu_list[num][4]
        stu_list[num][6] = stu_list[5]/3
        print("성적 수정이 완료되었습니다.\t")
        
# 4. 학생 성적 삭제

    elif choice ==4:
        print(" "*10,"[학생성적삭제]")
        print("-"*50)
        
        for idx, stus in enumerate(stu_list):
            print(f"{idx+1}{stus[0]}{stus[1]}")
        print("-"*50)
        
        try:
            del_choice = int(input("삭제하려는 번호를 입력하세요:"))
        except ValueError:
            print("올바른 숫자를 입력하세요.\t")
            continue
        
        try:
            flag = int(input(f"{stu_list[del_choice-1][0]} {stu_list[del_choice-1][1]} 학생이 맞습니까? 1.YES 2.NO"))
        except ValueError:
            print("1 or 2를 입력하세요.\t")
            continue
        if flag ==2:
            print("삭제가 취소 되었습니다.\t")
            continue
        
        del stu_list[del_choice-1]
        print("삭제가 완료되었습니다.\t")
        
    elif choice == 0:
        print("프로그램을 종료 합니다. 감사합니다!")
        break
    
    else:
        print("올바른 번호를 입력하세요.\t")
        
# 5. 등수만들기