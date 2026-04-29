import random

english = {
    '사랑': 'love',
    '커피': 'coffee',
    '컴퓨터': 'computer',
    '이름': 'name',
    '한국': 'korea',
    '학교': 'school',
    '음악': 'music',
    '책': 'book',
    '차': 'car',
    '전화': 'phone',
    '하늘': 'sky',
    '바다': 'sea',
    '산': 'mountain',
    '친구': 'friend',
    '동물': 'animal',
    '의자': 'chair',
    '책상': 'desk',
    '물': 'water',
    '불': 'fire'
}

# 20문제 중 랜덤으로 5문제 선택
quiz_list = random.sample(list(english.keys()), 5)

count = 0  # 맞춘 문제 수
results = []  # 정답/오답 기록

print("영어 맞추기 퀴즈! 총 5문제입니다.\n")

for idx, k in enumerate(quiz_list, start=1):
    print(f"{idx}. '{k}' 은(는) 영어로 뭘까요?")
    answer = input(">> ")

    # 정답 확인
    if answer.lower() == english[k].lower():
        print("정답! ")
        count += 1
        results.append("정답")
    else:
        print(f"틀렸습니다. 정답은 '{english[k]}'입니다.")
        results.append("오답")

# 문제별 결과 출력
print("문제별 결과:")
for i, r in enumerate(results, start=1):
    print(f"{i}. {r}")

# 총점 출력
print(f"\n총 {count}개 맞췄습니다. / 총 5개")



# a_list = [1,1,2,3,4,2,3,1,5,4]
# a_dic = {}

# for i in a_list:
#     if i in a_dic:        # 이미 딕셔너리에 있으면
#         a_dic[i] += 1     # 개수 +1
#     else:                 # 처음 나오는 값이면
#         a_dic[i] = 1      # 개수 1로 시작

# print(a_dic)