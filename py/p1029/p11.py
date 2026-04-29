import random

# a_list = [9,1,2,5,6,8,3,4,7]
# # # [3 * 3 리스트 형태]
# # b_list = []
# # for i, val in enumerate(a_list):
# #     print(val, end="\t")
# #     if (i+1)%3 == 0:
# #         print()



a_list = list(range(1,17))
random.shuffle(a_list)
print(a_list)

# 4 * 4 리스트 형태로 출력하시오.
for i, val in enumerate(a_list):
    print(val, end='\t')
    if (i + 1) % 4 == 0:
        print()
        
        
        
import random
# 3*3 리스트출력

a_list = list(range(1,10))
# 랜덤 섞기
random.shuffle(a_list)

print(a_list)
for idx, a in enumerate(a_list):
    print(a, end=' \t')
    if (idx+1) % 3 == 0:
        print()












# [3 * 3 리스트 형태]

# a_list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# print(a_list[0])


# b_list = [1,2,3]
# print(b_list[0])


# # [ [1,2,3], [4,5,6], [7,8,9] ]
# # 3*3 리스트 형태로 출력하시오. 8만 제거하시오.
# for aa in a_list: # [1,2,3] [4,5,6] [7,8,9]
#     for a in aa: # [1,2,3]
#         print(a, end=' \t')
#     print()




# print(a_list)
# ###############################################중요########################################
# b_list = list(range(1,10))
# print(b_list)
# ##############################################중요#########################################
# c_list = [i for i in range(1,10)]
# print(c_list)
# a_list = [1,2,3,4,5,6,7,8,9,10]

# # 리스트 자동화
# b_list = ['0','0','0','0','0','0','0','0','0','0']
# print(b_list)
# e_list = list('0; *9')
# print(e_list)
# f_list = ['0' for i in range(9)]
# print(f_list)


# a_list = list(range(1,10))
# b_list = []
# # [
#    # [ 1,2,3 ]
#     # [ 4,5,6 ]
#     # [ 7,8,9 ]
    
# # 1 2 3
# # 4 5 6
# # 7 8 9
# # print(a_list)
# for i in a_list:
#     print(i, end=' \t')
#     if i % 3 == 0:
#         print()
        
# 4*4 리스트형태로 출력하시오.
# [4*4 리스트 형태]
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# a_list = list(range(1, 17))
# for i in a_list:
#     print(i, end='\t')
#     if i % 4 == 0:
#         print()

# a_list = list(range(1, 26))
# for i in a_list:
#     print(i, end='\t')
#     if i % 5 == 0:
#         print()



        
        
        
