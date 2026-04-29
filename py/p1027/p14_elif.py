# num = int (input("숫자를 입력하세요."))
# print("입력한 숫자 : ",num)

# # 0보다 큰수입니다. 0보다 작은수입니다.
# # if~else

# if num>=0:
#     print("0보다 큰수입니다.")
# elif:
#     print("0 입니다.")
# else:
#     print("0보다 작은수입니다.")


# 70점 이상 통과
# 60점 이상 재시험
# 60점 미만 탈락

score = 70

if score>= 70:
    print("통과")
elif score>=60:
    print("재시험")
else:
    print("탈락")
    
    
# 90점이상 A, 80점 이상 B, 70점이상 C, 60점이상 D, 60점미만 F

# score = int(input("점수를 입력하세요."))

# if score>=90:
#     print("A")
# elif 90> score>=80:
#     print("B")
# elif 80> score>=70:
#     print("C")
# elif 70> score>=60:
#     print("D")
# else:
#     print("F")

score = int(input("점수를 입력하세요"))
if(score>=60):
    print("합격")
else:
    print("불합격")
    
if score>=60: print("합격")
else: print("불합격")

# result = "합격" if score>=60 else result="불합격"