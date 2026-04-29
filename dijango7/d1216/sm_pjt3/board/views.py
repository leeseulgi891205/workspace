from django.shortcuts import render, redirect
from board.models import Board
from member.models import Member

# 게시판 삭제
def delete(request,bno):
    # 게시글 가져오기
    qs = Board.objects.get(bno=bno)
    qs.delete()
    context = {'flag':2}
    return redirect('/board/list/')


# 게시판 상세보기
def view(request,bno):
    # 게시글 가져오기
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request,'board/view.html',context)


# 게시판 리스트
def list(request):
    # 게시글 모두 가져오기
    qs = Board.objects.all().order_by('-bgroup','bstep')
    context = {'list':qs}
    return render(request,'board/list.html',context)

# 게시판 글쓰기
def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    elif request.method == 'POST':
        id = request.session.get('session_id')
        member_qs = Member.objects.get(id=id)
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile','')
        # bgroup 값을 입력
        qs = Board.objects.create(btitle=btitle,bcontent=bcontent,member=member_qs,bfile=bfile)
        qs.bgroup = qs.bno
        qs.save()
        context = {'flag':'1'}
        return render(request,'board/write.html',context)
        