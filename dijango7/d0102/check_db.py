import sqlite3

db_path = r"c:\workspace\dijango7\d0102\mompjt\db.sqlite3"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 모든 테이블 목록 조회
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
tables = cursor.fetchall()

print("=" * 60)
print("데이터베이스 테이블 목록")
print("=" * 60)
for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
    count = cursor.fetchone()[0]
    print(f"{table[0]}: {count}개 행")

print("\n" + "=" * 60)
print("board_petpost 테이블 존재 여부:")
petpost_exists = any(table[0] == 'board_petpost' for table in tables)
print(f"{'✓ 존재함' if petpost_exists else '✗ 없음'}")
print("=" * 60)

conn.close()
