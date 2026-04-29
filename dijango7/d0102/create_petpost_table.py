import sqlite3

db_path = r"c:\workspace\dijango7\d0102\mompjt\db.sqlite3"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("=" * 60)
print("board_petpost, board_petcomment 테이블 생성")
print("=" * 60)

# board_petpost 테이블 생성
create_petpost = """
CREATE TABLE IF NOT EXISTS board_petpost (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    image VARCHAR(100),
    views INTEGER DEFAULT 0,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES accounts_user(id)
);
"""

# board_petcomment 테이블 생성
create_petcomment = """
CREATE TABLE IF NOT EXISTS board_petcomment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    author_id INTEGER NOT NULL,
    parent_id INTEGER,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES accounts_user(id),
    FOREIGN KEY (parent_id) REFERENCES board_petcomment(id),
    FOREIGN KEY (post_id) REFERENCES board_petpost(id)
);
"""

try:
    cursor.execute(create_petpost)
    print("✓ board_petpost 테이블 생성 완료")
except Exception as e:
    print(f"✗ board_petpost 생성 중 오류: {e}")

try:
    cursor.execute(create_petcomment)
    print("✓ board_petcomment 테이블 생성 완료")
except Exception as e:
    print(f"✗ board_petcomment 생성 중 오류: {e}")

conn.commit()
conn.close()

print("=" * 60)
print("✓ 테이블 생성 완료!")
print("=" * 60)
