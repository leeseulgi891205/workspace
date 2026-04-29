stu_list = [
    ['홍길동', 80, 90, 80, 250, 83.33],
    ['유관순', 90, 90, 90, 250, 83.33],
    ['이순신', 100, 100, 100, 300, 100.00]
    ]


titles = ['이름','국어','영어','수학','합계','평균',]

print(" "*50)
print( " "*15, "[ 학생성적프로그램 ]")
print("-"*60)
print("1. 학생성적입력")
print("2. 학생성적출력")
print("-"*50)
choice = int(input("원하는 번호를 입력하세요."))
print()
# 학생성적출력
print(" "*10,"[ 학생성적리스트 ]")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{}\t".format(*titles))
print("-"*50)
for stus in stu_list:
    print("{}\t{}\t{}\t{}\t{}\t{}\t".format(*stus))
print("-"*50)


# print(" "*50)
# print( " "*15, "[ 학생성적프로그램 ]")
# print("-"*60)
# print("1. 학생성적입력")
# print("2. 학생성적출력")
# print("-"*50)
# choice = int(input("원하는 번호를 입력하세요."))
# print()
# # 학생성적출력
# print(" "*10,"[ 학생성적리스트 ]")
# print("-"*50)
# print("{}\t{}\t{}\t{}\t{}\t{}\t".format(*titles))
# print("-"*50)