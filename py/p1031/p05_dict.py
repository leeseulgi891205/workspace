# {키:값}
stu_dic = {"no": 1, "name": "홍길동", "kor": 100}

# dict 추가
stu_dic['eng'] = 90

# dict 수정
stu_dic['kor'] = 10

# dict 삭제
del stu_dic['name']

# keys값만 출력 방법
print(stu_dic.keys())
print(list(stu_dic.keys()))
for k in stu_dic.keys():
    print("{} : {}".format(k, stu_dic[k]))

# values() 출력  ← 괄호 () 꼭 붙이기!!
print(stu_dic.values())           
print(list(stu_dic.values()))     
for i, v in enumerate(stu_dic.values()):
    print("{} , {}".format(i, v))  # 콤마 구분 출력

# items() 출력 - k,v
print(stu_dic.items())             # 튜플 형태로 출력
print(list(stu_dic.items()))
for k, v in stu_dic.items():
    print("{} : {}".format(k, v))

# 딕셔너리 출력 (get 사용 시 안전)
print(stu_dic.get('no'))
print(stu_dic.get('name'))   # 삭제되어서 None 출력
print(stu_dic.get('kor'))    # 10 출력
print(stu_dic.get('math'))   # 없는 키도 None 출력 (에러 X)

# 딕셔너리 정렬
import operator  # 🔹 itemgetter를 사용하려면 꼭 import 해야 함

names = {"홍길동": 100, "유관순": 80, "이순신": 90, "김구": 99, "강감찬": 95}

# reverse=True : 역순정렬, reverse=False : 순차정렬
# itemgetter(0): 키 기준, itemgetter(1): 값 기준
names2 = sorted(names.items(), key=operator.itemgetter(0), reverse=True)
print(names)
print(names2)

# 리스트 정렬
a_list = [1, 5, 9, 4, 3]
# sort() -> 리스트 자체를 정렬 (원본 변경)
# sorted() -> 정렬된 새 리스트 반환 (원본 그대로)
# a_list.sort()
a_list.reverse()  # 리스트 순서를 반대로 뒤집음 (정렬 아님)
# reverse=True : 역순정렬
b_list = sorted(a_list, reverse=True)
print(a_list)
print(b_list)

# 리스트의 최대/최소 값
print(max(a_list))
print(min(a_list))