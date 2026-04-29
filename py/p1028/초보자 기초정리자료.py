# 2중 for문 사용해서 00~99까지출력

for i in range(0, 10):
    for j in range(0, 10):
        print("{:02d}{:02d}".format(i, j), end=" ")
    print()