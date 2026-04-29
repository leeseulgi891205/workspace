# 국어,영어,수학점수를 입력받아
# 합계,평균을 출력하시오.
# 합계 : 299
# 평균 : 99.97 소수점2자리까지 출력

# num = input("국어점수를 입력하세요")
# num2 = input("영어점수를 입력하세요")
# num3 = input("수학점수를 입력하세요")

# print("합계 : %d" % (int(num)+int(num2)+int(num3)))
# print("평균 : %.2f" % ((int(num)+int(num2+int(num3)))))

# /t : 탭키-사이띄움, /n : 줄바꿈.

print("안녕/t하/n세요")

name = input("이름을 입력하세요.")
kor = int(input("국어점수를 입력하세요."))
eng = int(input("영어점수를 입력하세요."))
math = int(input("수학점수를 입력하세요."))


name2 = input("이름을 입력하세요.")
kor2 = int(input("국어점수를 입력하세요."))
eng2 = int(input("영어점수를 입력하세요."))
math2 = int(input("수학점수를 입력하세요."))

name3 = input("이름을 입력하세요.")
kor3 = int(input("국어점수를 입력하세요."))
eng3 = int(input("영어점수를 입력하세요."))
math3 = int(input("수학점수를 입력하세요."))

print
print(" "*15+"학생성적프로그램")
print("-"*50)
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)

print("%s\t%d\t%d\t%d\t%d\t%.2f\t" % (  name,kor,eng,math,(kor+eng+math),(kor+eng+math)/3  )  ) 
print("%s\t%d\t%d\t%d\t%d\t%.2f\t" % (  name2,kor2,eng2,math2,(kor2+eng2+math2),(kor2+eng2+math2)/3  )  ) 
print("%s\t%d\t%d\t%d\t%d\t%.2f\t" % (  name3,kor3,eng3,math3,(kor3+eng3+math3),(kor3+eng3+math3)/3  )  )