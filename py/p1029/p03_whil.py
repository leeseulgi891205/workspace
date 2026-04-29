# while

num = 1
while True:
        print("[학생성적프로그램]")
        print("[1. 학생성적입력]")
        print("[2. 학생성적출력]")
        print("[3. 학생성적수정]")
        print("0. 프로그램종료")
        print("-"*20)
        no = int(input("원하는 번호를 입력하세요."))
        # no = 0비교
        if no == 0:
            break
        elif no == 1:
            print("[학생성적입력]")
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
print("{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(name, kor, eng, math, avg, total))

elif choice == 3




# while 종료 후
print(stu_list)






# 5번 동안 숫자를 입력받아 합계를 출력하시오.

# sum = 0
# for _ in range(5):
#     num = int(input("숫자를 입력하시오."))
#     sum += num
# print("합계:", sum)

# #while 문을 사용해서 5번 동안 숫자를 입력받아 합계를 출력하시오.

# sum = 0
# i = 0
# while i < 5:
#     num = int(input("숫자를 입력하시오."))
#     sum += num
#     i += 1
# print("합계:", sum)

# # for문을 사용해서 1~10까지 합을 구하시오.

# sum = 0
# for i in range(1, 11): # 자동증감이 된다.
#     sum += i
# print("합계: ", sum)

# # while 문을 사용해서 1~10까지 합을 구하시오.

# sum = 0
# i = 1
# while i <= 10:
#     sum += i
#     i += 1 # 증감식을 추가
# print("합계: ", sum)
