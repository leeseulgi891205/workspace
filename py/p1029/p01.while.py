# ['홍길동' , 100,90,80,270,90,00] 

stu_list = [100,90,80,270,90,00]
name = input("이름을 입력하세요: ")
kor = int(input("국어 점수를 입력하세요: "))
eng = int(input("영어 점수를 입력하세요: "))
math = int(input("수학 점수를 입력하세요: "))
total = kor + eng + math
avg = total / 3
stu_list.append(name)
stu_list.append(kor)
stu_list.append(eng)
stu_list.append(math)
stu_list.append(total)
stu_list.append(avg)
print("이름\t국어\t영어\t수학\t합계\t평균\t")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(stu_list[0], stu_list[1], stu_list[2], stu_list[3], stu_list[4], stu_list[5]))