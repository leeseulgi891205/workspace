import os


# 1. 파일통로를 만듬(stream) : 파일열기
# r 모드 : read(읽기) 모드 w 모드 : write(쓰기) 모드 a 모드 : append(추가) 모드
f = open("studata.txt","r")
txt = f.readline()  # 파일내용 읽기
print(txt)