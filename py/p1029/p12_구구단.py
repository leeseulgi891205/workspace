# 구구단 프로그램 만들기
# 1. 구구단 출력


for i in range(2,10):
    if i%2 == 1:
        continue
    for j in range(1,10):
        print("[{}단]".format(i))
        if i%2 == 1:
            continue
        print("{} x {} = {}".format(i,j,i*j))
    print()
print("구구단 프로그램이 종료되었습니다. 이용해주셔서 감사합니다.")

# 무작위 구구단 출력 기능 추가
import random
random_dan = random.randint(2,9)
print(f"무작위로 선택된 구구단: {random_dan}단")
for j in range(1,10):
    print("{} x {} = {}".format(random_dan,j,random_dan*j))
print("구구단 프로그램이 종료되었습니다. 이용해주셔서 감사합니다.")
