# 함수를 여기에 생성
# 함수내에 사용할때 단순변수,복합변수에 따라 호출달라짐.
# 단순변수를 호출해서 값을 변경시 : global
# 복합변수는 호출해서 값을 변경가능

titles = ['번호','이름','국어','영어','수학','합계','평균','등수']
stu_list = [
    [10101,'홍길동',80,80,80,240,80.00,0],
    [10102,'유관순',90,90,90,280,90.00,0],
    [10103,'이순신',100,100,100,300,100.00,0]
] 
stu_list = [
    {'stuno':10101,'name':'홍길동','kor':80,'eng':80,'math':80,\
        'total':240,'avg':80.00,'rank':0},
    {'stuno':10102,'name':'유관순','kor':90,'eng':90,'math':90,\
        'total':270,'avg':90.00,'rank':0},
    {'stuno':10102,'name':'이순신','kor':100,'eng':100,'math':100,\
        'total':300,'avg':100.00,'rank':0},
] 
stu_count = 10104  #학생번호-단순변수


# 화면출력함수
def screen_print():
    print("-"*50)
    print(" "*10,"[ 학생성적프로그램 ]")
    print("-"*50)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("5. 등수처리")
    print("0. 프로그램종료")
    print("-"*50)

# 1.학생성적입력함수    
def stu_input():
    global stu_count        # 전역변수 사용
    print("[ 학생성적입력 ]")
    name = input("{}번 학생이름을 입력하세요.>> ".format(stu_count))
    kor = int(input("국어점수를 입력하세요.>> "))
    eng = int(input("영어점수를 입력하세요.>> "))
    math = int(input("수학점수를 입력하세요.>> "))
    total = kor+eng+math
    avg = total/3
    # 영어,수학,합계,평균 추가하기
    stu_list.append([stu_count,name,kor,eng,math,total,avg,0]) #등수
    stu_count = stu_count + 1 #학생번호1증가
    print("성적입력이 완료되었습니다.")
    print()  
    
# 2. 학생성적출력함수    
def stu_print():
    print(" "*10,"[ 학생성적리스트 ]")
    print("-"*50)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*titles))
    print("-"*50)
    for stus in stu_list:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(*stus))
    print()  

# 3. 학생성적수정함수    
def stu_modify():
    print(" "*10,"[ 학생성적수정 ]")
    print("-"*50)
    # 1. 10101 홍길동
    # 2. 10102 유관순
    # 3. 10103 이순신
    for idx,stus in enumerate(stu_list):
        print("{}. {} {}".format(idx+1,stus[0],stus[1]))
    print("-"*50)
    choice = int(input("수정하려는 번호를 입력하세요.>> ")) 
    # 1
    print("[ {} 학생 수정과목 선택 ]".format(stu_list[choice-1][1]))
    print("1. 국어점수")
    print("2. 영어점수")
    print("3. 수학점수")
    print("-"*50)
    subject = int(input("수정하려는 과목을 선택하세요.>> "))
    # 0=choice-1 [10101,'홍길동',80:subject+1=2,80,80,240,80.00]
    print("-"*50)
    print("현재 {}점수 : {} ".\
        format(titles[subject+1],stu_list[choice-1][subject+1]  ))
    print("-"*50)
    # 점수수정
    score = int(input("수정할 점수를 입력하세요.>> "))
    stu_list[choice-1][subject+1] = score
    # 합계수정
    stu_list[choice-1][5] = \
        stu_list[choice-1][2]+stu_list[choice-1][3]+stu_list[choice-1][4]
    # 평균수정
    stu_list[choice-1][6] = stu_list[choice-1][5]/3    
    
    print("{}점수 {}점으로 수정이 완료되었습니다.".\
        format(titles[subject+1],score))
    print(stu_list)
    print()

# 4. 학생성적삭제함수
def stu_delete():
    print(" "*10,"[ 학생성적삭제 ]")
    print("-"*50)
    # 1. 10101 홍길동
    # 2. 10102 유관순
    # 3. 10103 이순신
    for idx,stus in enumerate(stu_list):
        print("{}. {} {}".format(idx+1,stus[0],stus[1]))
    print("-"*50)
    choice = int(input("삭제하려는 번호를 입력하세요.>> "))
    flag = int(input("{} {} 학생이 맞습니까?(1.yes, 2.no)".\
        format(stu_list[choice-1][0],stu_list[choice-1][1])))
    if flag == 2:
        print("삭제가 취소되었습니다.")
        return # 함수에서 종료시 return 사용 , # 반복문에서 멈춤 : continue
    
    # 삭제부분
    del stu_list[choice-1]
    print("삭제가 되었습니다. ")
    print(stu_list)
    print()       

# 5. 등수처리함수
def rank():
    for s1 in stu_list:
        count = 1
        for s2 in stu_list:
            if s1[5] < s2[5]:
                count += 1
        s1[7] = count
    print("등수처리가 완료되었습니다.")
    print()    