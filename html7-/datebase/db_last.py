import db_latConn
from db_latConn import *

conn = db_latConn.getConnection()

print("연결: ", conn)

#------------------------------
while True:
    print("[1.학생성적정리프로그램]")