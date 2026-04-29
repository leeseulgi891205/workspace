# 로또 맞추기 프로그램을 구현하시오.

import random

# 1. 변수선언
my_list = []
c_list = []
count = 0


# 2. 6개 번호생성
lotto = random.sample(range(1, 46),6)
lotto.sort()
print("로또번호가 생성되었습니다. 숫자 6개를 입력해주세요.")
print("행운을 빕니다.")


# 3. 6개 번호입력
for i in range(6):
    while True:
        num = int(input(f"{i+1}번째 숫자(1~45)를 입력하세요: "))
        if not (1 <= num <= 45):
            print("1~45 사이의 숫자를 입력하세요.")
            continue 
        if num in my_list:
            print("중복된 숫자입니다. 다른 숫자를 적어주세요.")
            continue
        my_list.append(num)
        break


# 4. 번호확인
for i in lotto:
    if i in my_list:
        count += 1
        c_list.append(i)

# 5. 결과출력
print("\n[결과화면]")
print("-"*50)
print("로또번호", lotto)
print("내 번호", my_list)
print("당첨번호", c_list)
print("맞춘개수", count, "개")

# 5. 당첨금 출력
print("[당첨결과]")
if count ==2:
    print("축하합니다. 5등 당첨. [5,000원]")
elif count ==3:
    print("축하합니다. 4등 당첨. [50,000원] ")
elif count ==4:
    print("축하합니다. 3등 당첨. [5,000,000원]")
elif count ==5:
    print("축하합니다. 2등 당첨. [100,000,000원]")
elif count ==6:
    print("축하합니다 1등 당첨!!!!!! [2,000,000,000원]")
else:
    print("낙첨입니다. 다음에 도전해주세요.")