from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from .models import Board, Comment
from member.models import Member
from django.urls import reverse
from django.db.models import F, Q

# 게시판 리스트
def blist(request):
    qs = Board.objects.all().order_by('-bgroup', 'bstep')
    context = {'list':qs}
    return render(request,'board/list.html',context)

def view(request, bno):
    if request.method == 'GET':
        print("url view 호출")
        board = Board.objects.get(bno=bno)
        board.bhit += 1
        board.save()
        comments = Comment.objects.filter(board=board).order_by('-cdate')
        context = {'board':board, 'comments':comments}
        return render(request,'board/상세보기.html',context)
    elif request.method == 'POST':
        # 수정저장이 완료되면
        context = {'flag':'1'}
        return render(request,'board/상세보기.html',context)
        

# 글쓰기화면/글쓰기저장
def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        id = request.session['session_id']
        member = Member.objects.get(id=id)
        
        # 게시글 생성
        board = Board.objects.create(
            btitle=btitle,
            bcontent=bcontent,
            member=member
        )
        
        # 파일이 업로드된 경우 처리
        if bfile:
            import os
            from django.conf import settings
            
            # media/board 디렉토리 생성
            upload_dir = os.path.join(settings.MEDIA_ROOT, 'board')
            os.makedirs(upload_dir, exist_ok=True)
            
            # 파일명 설정 (중복 방지를 위해 bno 포함)
            file_ext = os.path.splitext(bfile.name)[1]
            filename = f"board_{board.bno}{file_ext}"
            file_path = os.path.join(upload_dir, filename)
            
            # 파일 저장
            with open(file_path, 'wb+') as destination:
                for chunk in bfile.chunks():
                    destination.write(chunk)
            
            # 파일 경로를 DB에 저장
            board.bfile = f"board/{filename}"
        
        # bgroup을 bno로 설정 (원글은 자신의 bno가 bgroup)
        board.bgroup = board.bno
        board.save()
        
        context = {'flag':'1'}
        return render(request,'board/write.html',context)

# 게시글 수정
def update(request, bno):
    board = Board.objects.get(bno=bno)
    if request.method == 'GET':
        context = {'board': board}
        return render(request, 'board/update.html', context)
    elif request.method == 'POST':
        board.btitle = request.POST.get('btitle')
        board.bcontent = request.POST.get('bcontent')
        board.save()
        # 2. 검색된 데이터에서 .bstep을 뽑아서 1씩 증가
        return render(request, 'board/update.html', {'board': board, 'update_state': '1'})

# 게시글 삭제
def delete(request, bno):
    Board.objects.get(bno=bno).delete()
    qs = Board.objects.all().order_by('-bno')
    context = {'list': qs, 'delete_state': '1'}
    return render(request, 'board/list.html', context)

# 댓글 추가
def comment_write(request, bno):
    if request.method == 'POST':
        board = Board.objects.get(bno=bno)
        ccontent = request.POST.get('ccontent')
        id = request.session.get('session_id')
        if id:
            member = Member.objects.get(id=id)
            Comment.objects.create(
                board=board,
                member=member,
                ccontent=ccontent
            )
    return redirect('board:view', bno=bno)

# 댓글 삭제
def comment_delete(request, cno, bno):
    Comment.objects.get(cno=cno).delete()
    return redirect('board:view', bno=bno)

# 답글달기
def reply(request, bno):
    board = Board.objects.get(bno=bno)
    if request.method == 'GET':
        context = {'board': board}
        return render(request, 'board/reply.html', context)
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        id = request.session['session_id']
        member = Member.objects.get(id=id)
        
        # 답변달기 저장
        # 같은 bgroup에서 bstep보다 큰 것들을 +1 증가
        Board.objects.filter(bgroup=board.bgroup, bstep__gt=board.bstep).update(bstep=models.F('bstep')+1)
        
        # 답글 생성
        reply_board = Board.objects.create(
            btitle=btitle,
            bcontent=bcontent,
            member=member,
            bgroup=board.bgroup,
            bstep=board.bstep + 1,
            bindent=board.bindent + 1
        )
        
        return redirect('board:view', bno=reply_board.bno)

