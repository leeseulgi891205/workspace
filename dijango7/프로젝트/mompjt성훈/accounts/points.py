# /mnt/data/mompjt/accounts/points.py

# 활동별 기본 포인트
POINT_RULES = {
    "login": 1,
    "quest_complete": 3,

    # ✅ 글/댓글 작성 보상 (1번)
    "post_create": 5,
    "comment_create": 2,
}

# ✅ 등급별 포인트 보너스(진짜 혜택 B)
# user.grade 코드: start/join/talk/empathy/core
GRADE_POINT_MULTIPLIER = {
    "start": 1.00,    # 🌱 시작
    "join": 1.05,     # ✍ 참여
    "talk": 1.10,     # 💬 소통
    "empathy": 1.15,  # 🤝 공감
    "core": 1.20,     # ⭐ 핵심
}

def _apply_grade_bonus(user, base: int) -> int:
    if base <= 0:
        return 0
    grade = getattr(user, "grade", "start") or "start"
    mul = GRADE_POINT_MULTIPLIER.get(grade, 1.00)

    # 정수 포인트로 지급 (반올림)
    return int(round(base * mul))

def add_point(user, action: str, save=True) -> int:
    base = POINT_RULES.get(action, 0)
    if base <= 0:
        return 0

    p = _apply_grade_bonus(user, base)

    user.point = (user.point or 0) + p
    if save:
        user.save(update_fields=["point"])
        user.recalc_grade(save=True)
    return p
