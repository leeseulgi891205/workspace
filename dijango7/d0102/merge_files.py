import shutil
import os
from pathlib import Path
from datetime import datetime

# 경로 설정
source_dir = Path(r"c:\workspace\dijango7\d0102\mompjt수정")
target_dir = Path(r"c:\workspace\dijango7\d0102\mompjt")
backup_dir = Path(r"c:\workspace\dijango7\d0102\mompjt_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S"))

print("=" * 70)
print("파일 및 폴더 병합 시작 (mompjt수정 → mompjt)")
print("=" * 70)

# 1단계: 전체 폴더 백업
print("\n[1단계] mompjt 전체 백업 중...")
shutil.copytree(target_dir, backup_dir, dirs_exist_ok=True)
print(f"✓ 백업 완료: {backup_dir}")

# 2단계: 파일 병합 통계
print("\n[2단계] 파일 병합 시작...")
stats = {
    'copied': 0,
    'overwritten': 0,
    'skipped': 0,
    'errors': 0
}

# 제외할 파일/폴더 (DB, 백업, 캐시 등)
exclude_items = {
    'db.sqlite3',
    'db.sqlite3.backup',
    '__pycache__',
    '.pyc',
    'node_modules',
    '.git',
    '.gitignore'
}

def should_skip(path_obj):
    """제외 항목 확인"""
    name = path_obj.name
    if name.endswith('.pyc') or name.startswith('.'):
        return True
    if name in exclude_items:
        return True
    if '__pycache__' in str(path_obj):
        return True
    return False

# 모든 파일 순회
for source_file in source_dir.rglob('*'):
    if should_skip(source_file):
        stats['skipped'] += 1
        continue
    
    # 상대 경로 계산
    relative_path = source_file.relative_to(source_dir)
    target_file = target_dir / relative_path
    
    try:
        if source_file.is_dir():
            # 디렉토리 생성
            target_file.mkdir(parents=True, exist_ok=True)
        elif source_file.is_file():
            # 디렉토리 생성
            target_file.parent.mkdir(parents=True, exist_ok=True)
            
            # 파일 복사
            if target_file.exists():
                # 기존 파일 덮어쓰기
                shutil.copy2(source_file, target_file)
                stats['overwritten'] += 1
                print(f"  ↻ {relative_path} (덮어쓰기)")
            else:
                # 새 파일 추가
                shutil.copy2(source_file, target_file)
                stats['copied'] += 1
                print(f"  ✓ {relative_path} (새로 추가)")
    except Exception as e:
        stats['errors'] += 1
        print(f"  ✗ {relative_path} - 오류: {str(e)}")

# 3단계: 결과 요약
print("\n" + "=" * 70)
print("[결과 요약]")
print("=" * 70)
print(f"✓ 새로 추가된 파일/폴더: {stats['copied']}개")
print(f"↻ 덮어쓴 파일: {stats['overwritten']}개")
print(f"- 제외된 항목: {stats['skipped']}개")
if stats['errors'] > 0:
    print(f"✗ 오류 발생: {stats['errors']}개")

print("\n" + "=" * 70)
print("✓ 파일 병합 완료!")
print("=" * 70)
print(f"\n대상 디렉토리: {target_dir}")
print(f"백업 디렉토리: {backup_dir}")
print("\n참고: 병합이 실패한 경우 백업에서 복구할 수 있습니다.")
