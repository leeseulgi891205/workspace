import oracledb

# 연결함수
def getConnection():
    return oracledb.connect\
    (user="ora_user", password="1111", dsn="localhost:1521/xe")
    
# db 연결
conn = getConnection()  ## sql 실행
cursor = conn.cursor()  ## 창



query = "select * from member"
cursor.execute(query)
# 데이터를 가져옴
rows = cursor.fetchall()
print(f"아이디\t비밀번호\t이름\t전화번호\t이메일\t성별\t취미")
print("-"*65)

for row in rows:
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*row))
    
    
# [[aaa,1111], [bbb,2222], [ccc,3333]]

    

print("DB 연결 성공",conn)

# 연결 종료
cursor.close()
conn.close()

