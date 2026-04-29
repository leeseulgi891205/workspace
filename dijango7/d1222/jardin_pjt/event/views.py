from django.shortcuts import render

# Create your views here.

def list(request):
    """이벤트 목록 페이지"""
    return render(request, 'event/list.html')
