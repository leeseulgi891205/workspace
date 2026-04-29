# 로또번호 맞추기 프로그램
# 1. 변수선언
# 2. 로또번호 생성
# 3. 숫자입력
# 4. 당첨여부 확인
# 5. 결과출력
# 6. 당첨금 출력

# 게임 개발: 주사위 굴리기, 카드 섞기, 무작위 아이템 드롭 등 게임의 무작위 요소를 구현하는 데 사용됩니다.
# 시뮬레이션: 무작위 현상에 기반한 과학적, 통계적 시뮬레이션을 만들 때 활용됩니다.
# 데이터 처리 및 분석: 데이터 샘플링, 데이터셋 섞기(셔플) 등에 사용됩니다.
# 보안 및 암호화: 일부 용도로 난수를 사용하지만, 더 높은 보안이 필요한 경우에는 secrets 모듈이 더 적합합니다.
# 기타: 무작위 비밀번호 생성, 음악 재생 순서 섞기 등 다양한 무작위 작업을 처리합니다.

import random # 프로그램에 난수(무작위 숫자) 생성 기능을 추가하기 위해서

# 1. 변수선언
my_list = []  # 입력한 번호
c_list = []   # 맞춘번호
count = 0     # 맞춘갯수

# 2. 로또번호 생성
lotto = random.sample(range(1, 46), 6)
lotto.sort()
print("로또번호가 생성되었습니다. 숫자 6개를 입력하세요.")
print("행운을 빕니다.")

# 3. 숫자입력 (6개)
for i in range(6):
    while True:
        num = int(input(f"{i+1}번째 숫자(1~45)를 입력하세요: "))
        # 문법 오류 수정: if i in range(6) (1 <= num <= 45): → if not (1 <= num <= 45):
        if not (1 <= num <= 45):
            print("1~45 사이의 숫자를 입력하세요.")
            continue # 특정 조건이 만족되었을 때 현재 반복을 즉시 건너뛰고 다음 반복을 계속 진행하도록 하는 역할
        if num in my_list:
            print("중복된 숫자입니다. 다른 숫자를 적어주세요.")
            continue
        my_list.append(num)
        break

my_list.sort()

# 4. 당첨여부 확인
for i in lotto:
    if i in my_list:
        count += 1
        c_list.append(i)

# 5. 결과출력
print("\n[결과화면]")
print("-" * 50)
print("로또번호:", lotto)
print("내 번호 :", my_list)
print("당첨번호:", c_list)
print("맞춘개수:", count, "개")

# 6. 당첨금 출력
print("\n[당첨 결과]")
if count == 2:
    print("축하합니다! 5등 당첨 - 5,000원")
elif count == 3:
    print("축하합니다! 4등 당첨 - 50,000원")
elif count == 4:
    print("축하합니다! 3등 당첨 - 5,000,000원")
elif count == 5:
    print("축하합니다! 2등 당첨 - 50,000,000원")
elif count == 6:
    print("축하합니다! 1등 당첨 엄청난걸요?? - 2,000,000,000원!!!")
else:
    print("낙첨입니다. 다음 기회에!")