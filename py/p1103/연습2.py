import random

# 로또 당첨 번호 (1~45 사이의 숫자 6개 무작위)
lotto = sorted(random.sample(range(1, 46), 6))
print("로또 당첨 번호:", lotto)

# 내 로또 번호 자동 생성 (1개)
my_lotto = sorted(random.sample(range(1, 46), 6))
print("내 로또 번호:", my_lotto)

# 맞춘 개수 계산
count = 0
for num in my_lotto:
    if num in lotto:
        count += 1

# 결과 출력
print(f"맞춘 개수: {count}개")

# 보너스 (선택)
if count == 6:
    print("1등! 모두 맞췄습니다!")
elif count == 5:
    print("2등! 5개 맞췄어요!")
elif count == 4:
    print("3등! 4개 맞췄어요!")
elif count == 3:
    print("4등! 3개 맞췄어요!")
else:
    print("꽝입니다. 다음 기회에...")
