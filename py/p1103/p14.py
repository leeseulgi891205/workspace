# 로또 맞추기 프로그램
# 로또 1개를 자동번호 추출로 입력받아,
# 몇개가 맞았는지 출력하시오.

import random

# 로또번호

lotto = random.sample(range(1,46),6)
print(lotto)
count = 0

# 자동추출 6개 my 번호

my_lottos = []
for i in range(6):
    my_lottos.append(random.sample(range(1,46),6))
print(my_lottos)
print("맞춘 개수: ")
for my_lotto in my_lottos:
    count = 0
    for num in my_lotto:
        if num in lotto:
            count += 1
    print("내 로또 번호: ",my_lotto,"맞춘 개수: ",count)
    break

# 자동추출 6개 함수

my_lottos.sort()
for i in lotto:
    if i in my_lotto:
        count += 1
    my_lottos.append(i) 
print("맞춘 개수: ",count)

# 번호비교
def cal():
    for num in my_lotto:
        if num in lotto:
            count += 1
            print("맞춘 개수: ",count)



        


