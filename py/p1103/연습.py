from stuFunc import * # stuFunc 모듈의 모든 함수 가져오기
from stuFunc import stu_print  # stuFunc 모듈에서 stu_print 함수만 가져오기


def screen_print():
    print("-"*50)
    print("학생성적관리프로그램")
    print("-"*50)
    print("-"*30)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("0. 프로그램종료")    


# 학생성적 프로그램

while True:
    screen_print()  # 함수호출
    choice = int(input("원하는 번호를 입력하세요."))
    
    if choice == 1:   # 학생성적 입력부분
        stu_print()
    elif choice == 2:  # 학생성적 출력부분
        stu_print()
        
        
        
# 함수를 이용해 학생성적 프로그램을 구성하시오.
# stuFunc.py 파일을 생성해 함수로 구성.
# stu_print() - 학생성적 입력부분
# stu_print() - 학생성적 출력부분

# 학생성적 프로그램
while True:
    screen_print()  # 함수호출
    choice = int(input("원하는 번호를 입력하세요."))
    
    if choice == 1:   # 학생성적 입력부분
        stu_print()
    elif choice == 2:  # 학생성적 출력부분
        stu_print()
        

def lotto_manual():
    lotto = []
    while len(lotto) < 6:
        num = int(input("1~45 사이의 숫자를 입력하세요."))
        if num < 1 or num > 45:
            print("1~45 사이의 숫자를 입력하세요.")
            continue
        if num in lotto:
            print("중복된 숫자입니다. 다시 입력하세요.")
            continue
        lotto.append(num)
    lotto.sort()
    return lotto
user_lotto = lotto_manual()
print("로또 번호: ",user_lotto)
def lotto_count(auto, manual):
    count = 0
    for num in manual:
        if num in auto:
            count += 1
    return count
atuo_lotto = lotto_auto()
manual_lotto = lotto_manual()
count = lotto_count(atuo_lotto, manual_lotto)
print("자동 로또 번호: ",atuo_lotto)
print("수동 로또 번호: ",manual_lotto)
print("맞춘 개수: ",count)