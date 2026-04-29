import oracledb
def getConnection():
    return oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
# db연결실행
conn = getConnection()
cursor = conn.cursor()
query = "select phone from member"
cursor.execute(query)
rows = cursor.fetchall()
# 1. member테이블에서 phone컬럼을 분리해서 가져와서 출력
# 국번  전화번호1  전화번호2
#------------------------------
# 527   250      1397
sql = "select phone from member"
cur = conn.cursor()
cur.execute(sql)
print(f"국번\t전번1\t전번2")
print("------------------------------")
for (phone,) in cur:
    parts = phone.split('-')
    if len(parts) == 3:
        area, mid, last = parts
    else:
        area = mid = last = "invalid"
    print(f"{area:<8}{mid:<10}{last}")
print("\n")




# 2. member테이블에서 phone컬럼을 가져와서 파이썬에서 분리해서 출력
# 국번  전화번호1  전화번호2
#------------------------------
# 527   250      1397
sql = "select phone from member"
cur = conn.cursor()
cur.execute(sql)
print(f"국번\t전번1\t전번2")
print("-"*50)
for row in rows:
    print(row)
    r = row[0].split("-")
    print("{}\t{}\t{}".format(*r))
print("연결 : ",conn)
conn.close()