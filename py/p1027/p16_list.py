# fruit = ["사과","배","수박","딸기","포도"]
# # 삭제
# # 해당되는 과일을 삭제하시오.
# print("리스트 과일종류 : ",fruit)
# input1 = input("삭제할 과일을 입력하세요")
# if input1 in fruit: # 리스트 안에 해당되는 글자가 있는지 확인(in)
#     fruit.remove(input1)
# else:
#     print("해당되는 과일이 없습니다.")
# fruit.remove(input1)
# print("리스트 과일종류:",fruit)






# input1 = input("좋아하는 과을 입력하세요")
# fruit.append(input1)
# print("입력과일종류 :"fruit)

#
# str1 = "안녕하세요"

# if "하" in str1:
#     print("존재합니다.")
# else:
#     print("하라는 글자가 존재하지 않습니다.")



########################중요#######################
str1 = "안녕하세요. 반갑습니다. 저는 홍길동입니다."
# 1개의 글자를 입력받아, str1 변수에 존재하는지 확인하시오.
print(" [해당문자열]")
input1 = input("1개의 글자를 입력하세요.")
# 입력값: 하, 존재합니다.

if input1 in str1:
    print("존재합니다.")
else:
    print("하라는 글자가 존재하지 않습니다.")