from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("메인 페이지에 오신 것을 환영합니다!")
