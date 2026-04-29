# 반복문에는 for문과 while문이 있다.
# for 변수 in 범위:
#while thue: # 무한루프

# while 조건: 

# for i in range(10):
#     print(i)
    
# i = 0 # 초기값
# while i < 10: # 조건식 - 조건이 맞을때까지 계속 실행
#     print(i) 
#     i += 1 # 증감식

i = 1
while i != 0:
    i = int(input("숫자를 입력하세요: (0입력: 종료)"))
    print("입력한 값: ", i)
print("[프로그램이 종료되었습니다. 다시 실행하세요.]")


num = 1
for _ in range(100000):
    num = int(input("숫자를 입력하세요. (0입력: 종료)"))
    if num == 0: break
    print("입력한 값: ", num)
print("[프로그램이 종료되었습니다. 다시 실행하세요.]")