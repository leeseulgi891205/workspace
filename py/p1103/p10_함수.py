# 기본매개변수 - 호출함수(매개변수) 개수가와 함수정의 매개변수 개수가 같아야함.
# 가변매개변수 - 기본매개변수가 앞에 오고, 뒤에 가변매개변수가 오면 매개변수 개수가 달라도 됨.
# *매개변수 라고 하면 됨.
# 키워드 매개변수.
# 키워드매개변수 - 변수에 미리 값을 할당 b=10, b의 값이 들어오면 들어온 값 할당
#                b의 값이 없으면 기본 10값으로 세팅.
# 키워드 매개변수는 기본매개변수와 같이 사용됨.

# def func(a,b=10):
#     print(a,b)
    
# func(20,10)
# func(20) # 할당이 되지 않으면 b=10 라는 초기값을 할당함.
#def func(a,*b):
#    print(a)
#    for i in b:
#        print(i)
        
#func(1,2,3,4,5)
#func(10) # 할당이 되지 않으면 b=10 라는 초기값을 할당함.

def func(*a,b=10):
    print(b)
    for i in a:
        print(i)

func(10,1,2,3,4,5,b=1)










# from stuFunc import * # stuFunc 모듈의 모든 함수 가져오기
# from stuFunc import stu_print  # stuFunc 모듈에서 stu_print 함수만 가져오기


# def screen_print():
#     print("-"*50)
#     print("학생성적관리프로그램")
#     print("-"*50)
#     print("-"*30)
#     print("1. 학생성적입력")
#     print("2. 학생성적출력")
#     print("3. 학생성적수정")
#     print("4. 학생성적삭제")
#     print("0. 프로그램종료")    


# # 학생성적 프로그램

# while True:
#     screen_print()  # 함수호출
#     choice = int(input("원하는 번호를 입력하세요."))
    
#     if choice == 1:   # 학생성적 입력부분
#         stu_print()
#     elif choice == 2:  # 학생성적 출력부분
#         stu_print()