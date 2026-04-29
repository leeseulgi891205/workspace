titles = ['번호','이름','국어','영어','수학','합계','평균','등수']
stu_list = [
    [10101,'홍길동',80,80,80,240,80.00,0],
    [10102,'유관순',90,90,90,280,90.00,0],
    [10103,'이순신',100,100,100,300,100.00,0]
]

# 등수처리
for s1 in stu_list:
    count = 1
    for s2 in stu_list:
        if s1[5] < s2[5]:
            count += 1
    s1[7] = count


# 성적출력
print(" "*10,"[ 학생성적리스트 ]")
print("-"*65)
print(*titles,sep="\t")
print("-"*65)
for stus in stu_list:
    print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(*stus))
print()