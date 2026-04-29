from django.shortcuts import render

def write(request):
    # render - html 파일을 웹 브라우저에 보여주는 역할
    return render(request, 'write.html')
