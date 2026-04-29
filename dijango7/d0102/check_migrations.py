import sqlite3

db_path = r"c:\workspace\dijango7\d0102\mompjt\db.sqlite3"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("=" * 60)
print("Django 마이그레이션 기록")
print("=" * 60)

cursor.execute("SELECT * FROM django_migrations WHERE app='board' ORDER BY id;")
migrations = cursor.fetchall()

for migration in migrations:
    print(f"ID: {migration[0]}")
    print(f"App: {migration[1]}")
    print(f"Name: {migration[2]}")
    print(f"Applied: {migration[3]}")
    print()

print("=" * 60)
print("0009_petpost_petcomment 확인:")
exists = any(mig[2] == '0009_petpost_petcomment' for mig in migrations)
print(f"{'✓ 마이그레이션 기록 존재' if exists else '✗ 마이그레이션 기록 없음'}")
print("=" * 60)

conn.close()
