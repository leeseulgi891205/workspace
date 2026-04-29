from django.shortcuts import render, redirect
from board.models import Board
import datetime

# 게시글 작성
def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    elif request.method == 'POST':
        btitle = request.POST.get("btitle")
        bfile = request.FILES.get("bfile")  # file타입은 FILES로 받기
        # 이름을 변경해서 저장하기도 함
        # bfile = f'{datetime.datetime.now().microsecond}_{bfile}'
        print("post btitle 확인 : ",btitle)
        print("post bfile 확인 : ",bfile)
        print("날짜",datetime.datetime.now())
        print("날짜",datetime.datetime.now().microsecond)
        
        # 파일저장
        # qs = Board(btitle=btitle, bfile=bfile)
        # qs.save()
        
        # return redirect('/')
        return render(request,'board/write.html')
        
