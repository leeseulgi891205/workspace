import oracledb
#db연결함수선언

def getConnection():
    return oracledb.connect\
        (user="ora_user",password="1111",dsn="localhost:1521/xe")
        
while(True):
    print("1.입력")
    print("2.출력")
    print("3.수정")
    choice = input('원하는 번호를 입력하세요.>> ')
    if choice=="1":
        #db연결
        conn = getConnection()
        cursor = conn.cursor()
        
        # insert, update, delete
        #query = "insert into mamber values ()"
        #cursor.execute(query)
        #conn.commit()
        
        # select - 여려명, 1명 가능 
        query = "select * from mamber where id='aaa'"
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)
        
        conn.close()
        #db연결종료
        pass
    elif choice=="2":
        #db연결
        #db연결종료
        pass
    else:
        #db연결
        #db연결종료
        pass