from django.shortcuts import render
from django.http import HttpResponse

def write(request):
    # return HttpResponse("<html><body><h1>글쓰기 페이지</h1></body></html>")
    return render(request, 'write.html')
