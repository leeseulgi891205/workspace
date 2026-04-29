# stu_data = [] # 리스트
# stu_data.append(1)
# stu_data.append("홍길동")
# stu_data.append("100")
# stu_data.append("100")
# stu_data.append("100")
# print(stu_data)

stu_datas = []

name = input("이름을 입력하세요.")
kor = int(input("국어점수를 입력하세요."))
eng = int(input("영어점수를 입력하세요."))
math = int(input("수학점수를 입력하세요."))
total = kor+eng+math
avg = total/3
stu_data = [name,kor,eng,math,total,avg]
stu_datas.append(stu_data)
stu_datas.append(stu_data2)
stu_datas = [name,kor,eng,math,total,avg]

# 두번째 학생 성적
name2 = input("이름을 입력하세요.")
kor2 = int(input("국어점수를 입력하세요."))
eng2 = int(input("영어점수를 입력하세요."))
math2 = int(input("수학점수를 입력하세요."))
total2 = kor+eng+math
avg2 = total/3
stu_data2 = [name2,kor2,eng2,math2,total2,avg2]
print(stu_data2)
stu_datas.append(stu_data2)


# stu_datas출력
print("-"*50)
print(stu_datas)