import sqlite3
import shutil
from pathlib import Path

# 경로 설정
original_db = r"c:\workspace\dijango7\d0102\mompjt수정\db.sqlite3"
modified_db = r"c:\workspace\dijango7\d0102\db 수정.sqlite3"
backup_db = r"c:\workspace\dijango7\d0102\mompjt수정\db.sqlite3.backup"

print("=" * 60)
print("SQLite 데이터베이스 병합 시작")
print("=" * 60)

# 1단계: 원본 DB 백업
print("\n[1단계] 기존 db.sqlite3 백업 중...")
shutil.copy(original_db, backup_db)
print(f"✓ 백업 완료: {backup_db}")

# 2단계: 두 DB의 테이블 및 데이터 확인
print("\n[2단계] 데이터베이스 정보 확인 중...")

conn_original = sqlite3.connect(original_db)
conn_modified = sqlite3.connect(modified_db)
conn_original.row_factory = sqlite3.Row
conn_modified.row_factory = sqlite3.Row

cursor_original = conn_original.cursor()
cursor_modified = conn_modified.cursor()

# 테이블 목록 조회
cursor_original.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
original_tables = set(row[0] for row in cursor_original.fetchall())

cursor_modified.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
modified_tables = set(row[0] for row in cursor_modified.fetchall())

print(f"\n원본 DB (db.sqlite3) 테이블: {sorted(original_tables)}")
print(f"수정 DB (db 수정.sqlite3) 테이블: {sorted(modified_tables)}")

# 3단계: 테이블별로 데이터 병합
print("\n[3단계] 데이터 병합 중...")

# 원본 DB에 수정 DB의 데이터 추가
for table in modified_tables:
    if table.startswith('sqlite_'):
        continue
    
    try:
        # 테이블 구조 확인
        cursor_modified.execute(f"PRAGMA table_info({table})")
        columns = cursor_modified.fetchall()
        col_names = [col[1] for col in columns]
        pk_name = next((col[1] for col in columns if col[5]), None)  # primary key 찾기
        
        # 수정 DB에서 데이터 조회
        cursor_modified.execute(f"SELECT * FROM {table}")
        rows = cursor_modified.fetchall()
        
        if table in original_tables:
            # 두 테이블 모두 존재하는 경우 - 중복 제거하며 병합
            if pk_name:
                # Primary key가 있으면 ID 기준으로 병합
                cursor_original.execute(f"SELECT {pk_name} FROM {table}")
                existing_ids = set(row[0] for row in cursor_original.fetchall())
                
                placeholders = ','.join(['?' for _ in col_names])
                insert_sql = f"INSERT OR IGNORE INTO {table} ({','.join(col_names)}) VALUES ({placeholders})"
                
                insert_count = 0
                for row in rows:
                    try:
                        cursor_original.execute(insert_sql, row)
                        insert_count += 1
                    except Exception as e:
                        pass  # 중복 또는 제약 조건 위반 무시
                
                if insert_count > 0:
                    print(f"  ✓ {table}: {insert_count}개 행 추가")
            else:
                # Primary key가 없으면 전체 데이터 병합
                placeholders = ','.join(['?' for _ in col_names])
                insert_sql = f"INSERT OR IGNORE INTO {table} ({','.join(col_names)}) VALUES ({placeholders})"
                
                insert_count = 0
                for row in rows:
                    try:
                        cursor_original.execute(insert_sql, row)
                        insert_count += 1
                    except:
                        pass
                
                if insert_count > 0:
                    print(f"  ✓ {table}: {insert_count}개 행 추가 (또는 유지)")
        else:
            # 수정 DB에만 있는 테이블은 스킵
            print(f"  - {table}: 원본 DB에 없어서 스킵 (필요시 별도 처리)")
    
    except Exception as e:
        print(f"  ✗ {table} 처리 중 오류: {str(e)}")

# 4단계: 변경사항 커밋
conn_original.commit()
print("\n[4단계] 변경사항 저장 완료")

# 5단계: 병합 결과 확인
print("\n[5단계] 최종 데이터 확인...")
for table in original_tables:
    if not table.startswith('sqlite_'):
        cursor_original.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor_original.fetchone()[0]
        print(f"  {table}: {count}개 행")

# 연결 종료
conn_original.close()
conn_modified.close()

print("\n" + "=" * 60)
print("✓ 데이터베이스 병합 완료!")
print("=" * 60)
print(f"\n병합된 DB: {original_db}")
print(f"백업 위치: {backup_db}")
print("\n참고: 병합이 실패한 경우 백업에서 복구할 수 있습니다.")
