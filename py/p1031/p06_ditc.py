
english = {
    '사랑' : 'love',
    '커피' : 'coffee',
    '컴퓨터' : 'computer',
    '이름' : 'name',
    '한국' : 'korea'
}

# items() 출력 - k,v
# 영어 맞추기 프로그램을 구현하시오.


# 정답입력
count = 0
for k,v in english.items():
    print("{} 은(는) 영어로 뭘까요?".format(k))
    answer = input(">>")
    
    # 정답확인
    
    # answer == v
    if answer == v:
        print("정답!")
        count += 1
    else:
        print("틀렸습니다")
        
    
    # 1. 정답 2. 오답 3. 오답 4. 정답. 5. 정답
# 몇개 맞췄는지 출력
    print("정답",count)








names = ['홍','홍','김','이','유','이','홍','김','강','홍']

n_dic = {}

for i in n_dic:
    if i not in n_dic:
        n_dic[i] = 1
    else:
        n_dic[i] = n_dic[i] + 1
print(n_dic)







a_list = [1,2,3,1,1,2,1,3,4,5,]

a_dic = {}
b_dic = {}

# 반복 시키기
for i in a_list:
    if i not in a_dic:
        a_dic[i] = 1
    else:
        a_dic[i] = a_dic[i] + 1
print(a_dic)




# 1:0, 2:0, 3:0 딕셔너리를 추가 하시오.
# 2:5 딕셔너리를 추가하시오

a_dic = {1: 0, 2: 0, 3: 0}
print(a_dic)
a_dic[2] = 5
print(a_dic)


# '홍': 100, '이':90, '유':80 딕셔너리에 추가하시오.
# '이': 95 변경하시오.
# '유' 를 삭제하시오.
c_dic = {}

# 딕셔너리에 값 추가
c_dic['홍'] = 100
c_dic['이'] = 90
c_dic['유'] = 80

print(":", c_dic)

# '이' 값 변경
c_dic['이'] = 95
print(":", c_dic)

# '유' 삭제
del c_dic['유']
print(":", c_dic)





# 1:4, 2:2, 3:2, 4:1, 5:1
# for 변수 in 범위: - range,list,문자열,딕셔너리 - keys,items,튜플

for i in a_list:
    a_dic[i] = 0

print(a_dic)


딕셔너리 추가 방법은 없는 키를 입력하면 추가됩니다.
키 - 타입은 상관없음. str.int.float.bool,










중요 중요 중요#
해당값이 있는지 확인, 딕셔너리도 마찬가지
if 7 in a_list:
    print("존재")
else:
    print("없음")
    
a_dic = {'1':1,'2':3,'3':4}
if '1' in a_list:
    print('존재')
else:
    print('없음')
    
