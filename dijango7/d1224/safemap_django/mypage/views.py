from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from reports.models import Report

@login_required
def index(request):
    my_reports = Report.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "mypage/index.html", {"reports": my_reports})
