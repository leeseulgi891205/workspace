from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Report
from .forms import ReportForm
from .openai_utils import summarize_text

def main(request):
    reports = Report.objects.all()[:6]
    return render(request, "main.html", {"reports": reports})

@login_required
def create(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            # AI 요약 생성
            obj.summary = summarize_text(obj.content)
            obj.save()
            messages.success(request, "제보 등록 완료 ✅ (요약 자동 생성됨)")
            return redirect("main")
        messages.error(request, "제보 등록 실패. 입력값 확인 ㄱ")
    else:
        form = ReportForm(initial={"latitude": 37.535, "longitude": 126.97})
    return render(request, "reports/create.html", {"form": form})

def api_reports(request):
    qs = Report.objects.all()[:300]
    data = []
    for r in qs:
        data.append({
            "id": r.id,
            "title": r.title,
            "summary": r.summary,
            "lat": r.latitude,
            "lng": r.longitude,
            "status": r.status,
            "status_kr": r.get_status_display(),
        })
    return JsonResponse({"reports": data})

def _staff_check(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(_staff_check)
def admin_panel(request):
    reports = Report.objects.all()[:200]
    return render(request, "reports/admin_panel.html", {"reports": reports})

@user_passes_test(_staff_check)
def update_status(request, pk):
    r = get_object_or_404(Report, pk=pk)
    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in dict(Report.STATUS_CHOICES):
            r.status = new_status
            r.save(update_fields=["status"])
            messages.success(request, f"상태 변경 완료 ✅ (#{r.id})")
        else:
            messages.error(request, "상태값이 이상함. received/processing/done 중 하나.")
    return redirect("reports:admin_panel")
