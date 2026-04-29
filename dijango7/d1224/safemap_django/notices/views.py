from django.shortcuts import render, get_object_or_404
from .models import Notice

def list_view(request):
    notices = Notice.objects.all()[:30]
    return render(request, "notices/list.html", {"notices": notices})

def detail_view(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, "notices/detail.html", {"notice": notice})
