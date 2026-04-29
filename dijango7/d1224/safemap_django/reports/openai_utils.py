import os
from django.conf import settings

def summarize_text(text: str) -> str:
    """OpenAI 한 줄 요약. 키 없으면 fallback."""
    cleaned = (text or "").strip()
    if not cleaned:
        return "내용 없음"

    # Fallback: 키가 없거나 라이브러리 문제면 안전하게 짧게 자름
    if not getattr(settings, "OPENAI_API_KEY", ""):
        return (cleaned[:80] + "…") if len(cleaned) > 80 else cleaned

    try:
        from openai import OpenAI
        client = OpenAI(api_key=settings.OPENAI_API_KEY)

        # Responses API (권장)
        # - 프로젝트 성격상 '한 줄 요약'만 뽑음
        resp = client.responses.create(
            model=getattr(settings, "OPENAI_MODEL", "gpt-5-mini"),
            input=f"""다음 사건·사고 제보를 한국어로 '한 줄'로 요약해줘.
- 과장 금지
- 최대 60자
- 핵심만

제보:
{cleaned}
""",
        )
        # openai-python: resp.output_text 로 편하게 뽑을 수 있음(버전에 따라 다를 수 있어 방어)
        summary = getattr(resp, "output_text", None)
        if not summary:
            # fallback parse
            summary = str(resp)
        summary = (summary or "").strip().replace("\n", " ")
        if len(summary) > 120:
            summary = summary[:120] + "…"
        return summary or ((cleaned[:80] + "…") if len(cleaned) > 80 else cleaned)

    except Exception:
        return (cleaned[:80] + "…") if len(cleaned) > 80 else cleaned
