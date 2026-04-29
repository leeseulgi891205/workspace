import random
# 4*4 리스트출력

a_list = list(range(1,10))
# 랜덤 섞기
random.shuffle(a_list)
print(a_list)

# 무한반복 실행
while True:
    print("[ 좌표 맞추기 게임 ]")
    print('-'*30)
    for idx, a in enumerate(a_list):
        print(a, end=' \t')
        if (idx+1) % 3 == 0:
            print()
    print('-'*30)
    num = int(input("원하는 번호를 입력하세요."))
    # 9번을 입력받으면 9번자리가 X표시가 되어야 함.
    for a in enumerate(a_list):
        if a == num:
            a_list[idx] = "x"
            break
            

#---------------------------
# c_list = [1,2,3]
# c_list = [1] = 100