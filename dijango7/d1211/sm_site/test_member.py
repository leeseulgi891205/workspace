import os
import django

# Django 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smproject.settings')
django.setup()

from member.models import Member

try:
    # 회원 등록 테스트
    member = Member.objects.create(
        user_id='testuser01',
        pw='password123',
        name='테스트유저',
        phone='010-1234-5678',
        gender='남자',
        hobby='코딩'
    )
    
    print("✅ 회원 등록 성공!")
    print(f"ID: {member.user_id}")
    print(f"이름: {member.name}")
    print(f"전화번호: {member.phone}")
    print(f"\n현재 총 회원 수: {Member.objects.count()}명")
    
    # 모든 회원 조회
    print("\n=== 전체 회원 목록 ===")
    for m in Member.objects.all():
        print(f"- {m.user_id}: {m.name} ({m.phone})")
        
except Exception as e:
    print(f"❌ 오류 발생: {e}")
