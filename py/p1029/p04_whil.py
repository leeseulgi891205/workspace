# 이름, 국어, 점수를 입력 이름: 홍길동, 국어: 100 while문으로


print("[학생성적입력]")
name = input("이름을 입력하세요:")
print("이름을 입력하세요.")
kor = int(input("국어점수를 입력하세요."))
eng = int(inpur("영어점수를 입력하세요."))
math = int(inpur("수학점수를 입력하세요."))
print("이름: {},  ".format(name, kor))
print("이름: {},  ".format(kor))
print("이름: {},  ".format(eng))
print("이름: {},  ".format(math))


print("이름\t국어\t영어\t수학\t합계\t평균\t")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(name, kor, eng, math, kor+eng+math, (kor+eng+math)/3))