##############중요중요중요중요중요중요#####################

a_list = [1,1,2,3,4,2,3,1,5,4]
a_dic = {}
for i in a_list:
    if i not in a_dic:
        a_dic[i] = 1
    else:
        a_dic[i] += 1
        
print(a_dic)        
# {1:0,2:0,3:0,4:0,5:0}














# a_dic['홍길동'] = 100
# print(a_list)
# {'홍길동': 100}

# b_dic = {}
# b_dic[1] =1
# b_dic[2] =1
# b_dic[1] =10
# print(b_dic)
# # {1:1,2:1}












# b_dic = {}
# "홍길동": 100

# # 없는 키 입력시 추가
# b_dic['홍길동'] = 100

# # 있는 키입력시 수정
# b_dic['홍길동']

