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

# 20문제중에 랜덤으로 5문제를 뽑아서 퀴즈를 출력하시오.
a_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,]
quest = random.sample(a_list,5)   # 랜덤 5개를 뽑아오기. - 20 문제중 5개를 추출
quest.sort() # 랜덤 5개를 순서대로 정렬
quest_dic = {} # 정답인지 오답인지 알기위한 저장공간
# print(quest)

num = 1

for i, k,  in enumerate(english.keys()): # 인덱스 번호를 함께 추출 키값과 같이
    if i in quest: 
        # print(i,k,english[k])
        count = 0
        # 정답입력
        print("{} 은(는) 영어로 뭘까요?".format(k))
        answer = input(" >> ")
        # 정답확인
        if answer == english[k]:
            print("띵동! 정답입니다.")
            count += 1
            quest_dic[num] = "정답"   # i는 0번
        else:
            print("오답: ",english[k])
            quest_dic[num] = "오답"
        num += +1
print(quest_dic)
print("정답".count)