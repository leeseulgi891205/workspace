
# #"no":1, "name", "홍길동","kor":100 딕셔너리 추가해서 출력하시오.
# # 키 : 값 으로 모두 출력하시오.


# stu_dic = {"no":1,"name":"홍길동","kor":100}

# print(stu_dic['no']) = 1
# print(stu_dic['name']) = '홍길동'
# print(stu_dic['kor']) = 100

# print(stu_dic)
# for k,v in stu_dic.items ():
#     print("{}:{}".format(k,v))
    
# for k in stu_dic.keys():
#     print("{}:{}".format(k,stu_dic[k])) # no, stu_dic[no]
    
# for v in stu_dic.values():
#     print("값: {}".format(v))



stu_list = [
    {"no": 1, "name": "홍길동", "kor": 100},
    {"no": 2, "name": "유관순", "kor": 80},
    {"no": 3, "name": "이순신", "kor": 90}
]

# 3번째 학생(kor 점수)을 50점으로 변경
stu_list[2]["kor"] = 50


stus = {"no": 3, "name": "이순신", "kor": 90}



a_list = [3, '이순신', 90]
a_list[2] =50
print(a_list)
