# a_list = [1,2,3]
# # list추가 명령어 - append, insert, extend

# # append 제일뒤에 추가
# # 복합변수의 값이 변경이 됨.
# a_list.append(10)
# print(a_list)

# # insert - (위치,값)
# a_list.insert(1,200)
# print(a_list) #파괴적
# a2 = list = [5,6,7]
# a_list.insert(1.200)
# print(a_list)
# a2_list = [5,6,7]
# a_list.extend(a2_list) # 리스트 2개를 합침.
# print(a_list)

# a_list = a_list +[10,20,30]
# print(a_list)

# # list 값 변경 - 위치값을 입력하면 변경완료.
# a_list[2] = 1000
# # a_list[100] = # 없는 주소를 넣으면 에러가 남
# print(a_list)

# 삭제 -pop()-제일 뒤 삭제, del - 해당위치삭제, remove() - 해당값 삭제, clear - 모두삭제
aa_list = [1,2,3,4,5,6,7]
aa_list.pop()
print(aa_list)
del aa_list[0] # 해당위치 삭제
print(aa_list)
aa_list.remove(5) # 해당값 삭제
print(aa_list)
aa_list.clear()
print(aa_list) # 모두 삭제





a = 10 #비 파괴적
a + a + 100
print(a) # 값 10

# [] 1개 : 1차원 리스트
# [[]] 2개 : 2차원 리스트
# [[[]]] 3개 : 3차원 리스트


# 2차원 리스트 
b_list = [\
    ["홍길동",100,[1,2,3]], ["유관순",99], ["이순신",80], ["김구",89]]

print(b_list[0][2][1])