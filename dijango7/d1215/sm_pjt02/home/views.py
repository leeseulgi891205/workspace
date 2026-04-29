from django.shortcuts import render
from board.models import Board
from django.db.models import Q

def index(request):
    return render(request,'index.html')

def search(request):
    keyword = request.GET.get('keyword', '')
    search_type = request.GET.get('search_type', 'all')
    image_only = request.GET.get('image_only', '')
    
    # 기본 쿼리
    boards = Board.objects.all()
    
    # 검색 타입에 따른 필터링
    if keyword:
        if search_type == 'title':
            boards = boards.filter(btitle__icontains=keyword)
        elif search_type == 'content':
            boards = boards.filter(bcontent__icontains=keyword)
        else:  # all
            boards = boards.filter(Q(btitle__icontains=keyword) | Q(bcontent__icontains=keyword))
    
    # 이미지 있는 글만 필터링
    if image_only:
        boards = boards.exclude(bfile='')
    
    boards = boards.order_by('-bdate')
    
    context = {
        'boards': boards,
        'keyword': keyword,
        'search_type': search_type,
        'image_only': image_only,
        'count': boards.count()
    }
    return render(request, 'search_result.html', context)
