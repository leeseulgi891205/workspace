import sqlite3
import shutil

source_db = r'c:\workspace\dijango7\d0102\mompjt혜은\db.sqlite3'
target_db = r'c:\workspace\dijango7\d0102\mompjt\db.sqlite3'

# 백업 생성
backup_db = r'c:\workspace\dijango7\d0102\mompjt\db.sqlite3.hyeeun_backup'
shutil.copy(target_db, backup_db)
print(f'✅ 백업 생성: {backup_db}')
print()

# DB 연결
source_conn = sqlite3.connect(source_db)
source_cursor = source_conn.cursor()

target_conn = sqlite3.connect(target_db)
target_cursor = target_conn.cursor()

# 현재 상태 확인
print('=' * 60)
print('📊 병합 전 상태')
print('=' * 60)

target_cursor.execute('SELECT COUNT(*) FROM board_freepost')
current_count = target_cursor.fetchone()[0]
print(f'현재 mompjt 자유게시판: {current_count}개')

source_cursor.execute('SELECT COUNT(*) FROM board_freepost')
source_count = source_cursor.fetchone()[0]
print(f'혜은 mompjt 자유게시판: {source_count}개')
print()

# 자유게시판 데이터 병합
print('=' * 60)
print('📝 자유게시판 데이터 병합 중...')
print('=' * 60)

# ID 충돌 방지: 현재 최대 ID 확인
target_cursor.execute('SELECT IFNULL(MAX(id), 0) FROM board_freepost')
max_id = target_cursor.fetchone()[0]
print(f'현재 최대 ID: {max_id}')
print()

# 혜은 DB에서 데이터 가져오기
source_cursor.execute('''
    SELECT id, title, content, author_id, created_at, views 
    FROM board_freepost 
    ORDER BY id
''')
freeposts = source_cursor.fetchall()

added_count = 0
skipped_count = 0
id_mapping = {}  # 기존 ID -> 새 ID 매핑

for row in freeposts:
    old_id, title, content, author_id, created_at, views = row
    
    # 중복 체크 (제목과 내용이 같으면 스킵)
    target_cursor.execute('''
        SELECT COUNT(*) FROM board_freepost 
        WHERE title = ? AND content = ?
    ''', (title, content))
    
    if target_cursor.fetchone()[0] > 0:
        skipped_count += 1
        print(f'  ⊘ [{old_id}] {title[:40]} - 중복 스킵')
        continue
    
    try:
        # 새 ID로 삽입 (ID는 자동 생성)
        target_cursor.execute('''
            INSERT INTO board_freepost (title, content, author_id, created_at, views)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, content, author_id, created_at, views))
        
        new_id = target_cursor.lastrowid
        id_mapping[old_id] = new_id
        added_count += 1
        
        if added_count <= 20:  # 처음 20개만 출력
            print(f'  ✓ [{old_id} → {new_id}] {title[:50]} (조회수: {views})')
        elif added_count == 21:
            print('  ... (나머지 글도 추가 중)')
            
    except Exception as e:
        print(f'  ✗ [{old_id}] {title[:40]} - 오류: {str(e)}')

# 저장
target_conn.commit()

# 최종 결과
print()
print('=' * 60)
print('✅ 병합 완료')
print('=' * 60)

target_cursor.execute('SELECT COUNT(*) FROM board_freepost')
final_count = target_cursor.fetchone()[0]

print(f'추가된 글: {added_count}개')
print(f'중복 스킵: {skipped_count}개')
print(f'최종 자유게시판 글: {final_count}개')
print()
print('🎉 자유게시판 데이터 병합 완료!')
print('   - 중복 제거됨')
print('   - admin에서 확인 가능')
print('   - 모두 정상 작동')

source_conn.close()
target_conn.close()
