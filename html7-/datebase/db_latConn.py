import oracledb

def getConnection():
    return oracledb.connect\
        (user="ora_user", password="ora_password", dsn="localhost:1521/xe")