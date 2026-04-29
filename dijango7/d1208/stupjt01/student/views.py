from django.shortcuts import render

# 성정입력페이지 열기
def write(request):
    return render(request, 'write.html')


