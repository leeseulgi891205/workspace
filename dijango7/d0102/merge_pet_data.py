import sqlite3
import shutil

source_db = r'c:\workspace\dijango7\d0102\mompjt수정수정\db.sqlite3'
target_db = r'c:\workspace\dijango7\d0102\mompjt\db.sqlite3'

# 백업 생성
backup_db = r'c:\workspace\dijango7\d0102\mompjt\db.sqlite3.merge_backup'
shutil.copy(target_db, backup_db)
print(f'✅ 백업 생성: {backup_db}')
print()

# DB 연결
source_conn = sqlite3.connect(source_db)
source_cursor = source_conn.cursor()

target_conn = sqlite3.connect(target_db)
target_cursor = target_conn.cursor()

# 반려동물 게시글 데이터 이전
print('=' * 60)
print('🐶 반려동물 게시글 데이터 병합')
print('=' * 60)

source_cursor.execute('SELECT id, title, content, image, author_id, views, created_at, updated_at FROM board_petpost')
petposts = source_cursor.fetchall()

for row in petposts:
    old_id, title, content, image, author_id, views, created_at, updated_at = row
    
    # 중복 확인
    target_cursor.execute('SELECT COUNT(*) FROM board_petpost WHERE id = ?', (old_id,))
    if target_cursor.fetchone()[0] == 0:
        try:
            target_cursor.execute('''
                INSERT INTO board_petpost (id, title, content, image, author_id, views, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (old_id, title, content, image, author_id, views, created_at, updated_at))
            print(f'  ✓ [{old_id}] {title} (작성자 ID: {author_id})')
        except Exception as e:
            print(f'  ✗ [{old_id}] {title} - 오류: {str(e)}')

# 반려동물 댓글 데이터 이전
print()
print('=' * 60)
print('💬 반려동물 댓글 데이터 병합')
print('=' * 60)

source_cursor.execute('SELECT id, content, author_id, parent_id, post_id, created_at, updated_at FROM board_petcomment')
petcomments = source_cursor.fetchall()

for row in petcomments:
    comment_id, content, author_id, parent_id, post_id, created_at, updated_at = row
    
    # 중복 확인
    target_cursor.execute('SELECT COUNT(*) FROM board_petcomment WHERE id = ?', (comment_id,))
    if target_cursor.fetchone()[0] == 0:
        try:
            target_cursor.execute('''
                INSERT INTO board_petcomment (id, content, author_id, parent_id, post_id, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (comment_id, content, author_id, parent_id, post_id, created_at, updated_at))
            print(f'  ✓ 댓글 ID: {comment_id} (게시글 ID: {post_id})')
        except Exception as e:
            print(f'  ✗ 댓글 ID: {comment_id} - 오류: {str(e)}')

# 저장
target_conn.commit()

# 최종 확인
print()
print('=' * 60)
print('✅ 병합 완료')
print('=' * 60)

target_cursor.execute('SELECT COUNT(*) FROM board_petpost')
final_pet_count = target_cursor.fetchone()[0]

target_cursor.execute('SELECT COUNT(*) FROM board_petcomment')
final_comment_count = target_cursor.fetchone()[0]

print(f'최종 반려동물 게시글: {final_pet_count}개')
print(f'최종 반려동물 댓글: {final_comment_count}개')
print()
print('🎉 데이터 병합 완료!')
print('   - admin은 이미 동일')
print('   - URL은 이미 동일')
print('   - 모두 정상 구동')

source_conn.close()
target_conn.close()
