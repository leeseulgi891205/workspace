from django.shortcuts import render ,redirect
from customer.models import Board
from member.models import Member
from django.core.paginator import Paginator
from django.db.models import F,Q, Sum,Count


def clike(request):
    if request.method == 'POST':
        bno = request.GET.get('bno')
        board = Board.objects.get(bno=bno)
        id = request.session['session_id']
        member = Member.objects.get(id=id)
        # db : Board테이블에 likes컬럼에 데이터 추가,삭제
        if board.likes.filter(pk=member.pk).exists():
            board.likes.remove(member) # likes 안에 member 삭제
            board.likes_count = F('likes_count') - 1
        else:
            board.likes.add(member) # likes 안에 member 추가
            board.likes_count = F('likes_count') + 1
        board.save()
        
        
    context = {'result':'ok'}
    return render(request,'customer/clike.html',context)



def cwrite(request):
    if request.method == 'GET':
        return render(request, 'customer/cwrite.html')
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        
        # DB 저장 로직 추가 필요
        # board = Board(btitle=btitle, bcontent=bcontent, bfile=bfile)
        # board.save()
        qs = Board(btitle=btitle, bcontent=bcontent, bfile=bfile)
        qs.bgroup = qs.bno  # 새 글일 때는 bno가 그룹번호
        qs.save()
        return redirect('customer:clist')


def cepilog(request):
    return render(request, 'customer/inquiry_write.html')


def cinquiry_write(request):
    if request.method == 'POST':
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        
        qs = Board(btitle=btitle, bcontent=bcontent, bfile=bfile)
        qs.save()  # 먼저 저장해서 bno 생성
        qs.bgroup = qs.bno  # bno를 bgroup으로 설정
        qs.save()  # 다시 저장
        
        return redirect('customer:clist')
    return redirect('customer:cepilog')


def cview(request, bno):
    qs = Board.objects.get(bno=bno)
    
    # bgroup 역순정렬 , bstep 오름차순정렬
    
    # 이전글-------
    pre_qs = Board.objects.filter(Q(bgroup__lt=qs.bgroup)).order_by('-bgroup','bstep').first()
    # 답글달기가 포함 되어 있을때 쿼리문
    # pr_qs = Board.objects.filter(Q(bgroup=qs.bgroup) & Q(bstep__lt=qs.bstep)).order_by('-bgroup','bstep').first()
    print("이전글:",pre_qs)
    
    
    # 다음글-------
    next_qs = Board.objects.filter(bgroup__gt=qs.bgroup).order_by('bgroup','-bstep').first()
    # 답글달기가 포함 되어 있을때 쿼리문
    # next_qs = Board.objects.filter(Q(bgroup=qs.bgroup) & Q(bstep__gt=qs.bstep)).order_by('bgroup','bstep').first()
    print("다음글:",next_qs)
    
    
    
    context = {'c':qs,'pre_c':pre_qs,'next_c':next_qs}
    return render(request, 'customer/cview.html', context)


def clist(request):
    # 검색부분----------------------------------------------------------
    category = request.GET.get('category','')
    search = request.GET.get('search','')
    print("검색으로 넘어온 데이터 :",category,search)
    
    if not search:
        qs = Board.objects.all().order_by('-bgroup','bstep')
    else:
        if category == 'btitle':
            qs = Board.objects.filter(btitle__contains=search)
        elif category == 'bcontent':
            qs = Board.objects.filter(bcontent__contains=search)
        elif category == 'all':
            qs = Board.objects.filter(Q(btitle__contains=search))
    
    # 하단 페이지 넘버링 --------------------------------------------------
    # Paginator는 꼭 요청페이지 번호가 있어야함
    # 요청페이지번호 : int타입
    page = int(request.GET.get('page',1)) # 없으면 1번 페이지 호출
    paginator = Paginator(qs,10)
    list_qs = paginator.get_page(page)
    
    context = {'list':list_qs,'page':page,'category':category,'search':search}
    return render(request,'customer/clist.html',context)
