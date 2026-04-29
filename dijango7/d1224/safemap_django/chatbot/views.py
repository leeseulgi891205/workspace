import json
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def chat(request):
    return render(request, "chatbot/chat.html")

@csrf_exempt
def ask(request):
    # 심플: 키 없으면 mock 답변
    try:
        payload = json.loads(request.body.decode("utf-8"))
    except Exception:
        payload = {}
    q = (payload.get("q") or "").strip()
    if not q:
        return JsonResponse({"answer":"질문이 비어있음"}, status=400)

    if not getattr(settings, "OPENAI_API_KEY", ""):
        return JsonResponse({"answer": f"(모의응답) '{q}'에 대해: 제보를 등록하거나 공지를 확인해봐."})

    try:
        from openai import OpenAI
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        resp = client.responses.create(
            model=getattr(settings, "OPENAI_MODEL", "gpt-5-mini"),
            input=f"""너는 SafeMap 프로젝트 챗봇이야.
사용자 질문에 짧고 실용적으로 답해.
질문: {q}
"""
        )
        ans = getattr(resp, "output_text", None) or str(resp)
        ans = (ans or "").strip()
        return JsonResponse({"answer": ans[:600]})
    except Exception:
        return JsonResponse({"answer": "(오류) OpenAI 호출 실패. 키/모델/네트워크 확인 ㄱ"}, status=500)
