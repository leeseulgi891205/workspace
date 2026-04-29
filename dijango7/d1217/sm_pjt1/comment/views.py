from django.shortcuts import render
from comment.models import Comment
from board.models import Board
from member.models import Member
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def list(request):
    if request.method == 'POST':
        bno = request.POST.get('bno')
        
        # 해당 게시글의 댓글 가져오기
        comments = Comment.objects.filter(board__bno=bno).order_by('-cdate')
        
        # 댓글 리스트를 JSON 형식으로 변환
        comments_list = []
        for comment in comments:
            comments_list.append({
                'cno': comment.cno,
                'name': comment.member.name if comment.member else (comment.cname or '익명'),
                'ccontent': comment.ccontent,
                'cdate': comment.cdate.strftime('%Y-%m-%d %H:%M'),
                'is_member': True if comment.member else False
            })
        
        context = {
            'result': 'success',
            'comments': comments_list
        }
        return JsonResponse(context)
    
    return JsonResponse({'result': 'error', 'message': 'POST 요청만 가능합니다.'})

@csrf_exempt
def write(request):
    if request.method == 'POST':
        bno = request.POST.get('bno')
        ccontent = request.POST.get('ccontent')
        
        # 게시글 가져오기
        try:
            board = Board.objects.get(bno=bno)
            
            # 로그인 여부 확인
            if request.session.get('session_id'):
                # 로그인한 사용자
                member = Member.objects.get(id=request.session.get('session_id'))
                comment = Comment.objects.create(
                    board=board,
                    member=member,
                    ccontent=ccontent
                )
                name = member.name
            else:
                # 비회원 댓글
                cname = request.POST.get('cname')
                cpw = request.POST.get('cpw')
                
                if not cname or not cpw:
                    return JsonResponse({'result': 'error', 'message': '이름과 비밀번호를 입력해주세요.'})
                
                comment = Comment.objects.create(
                    board=board,
                    cname=cname,
                    cpw=cpw,
                    ccontent=ccontent
                )
                name = cname
            
            return JsonResponse({
                'result': 'success',
                'comment': {
                    'cno': comment.cno,
                    'name': name,
                    'ccontent': comment.ccontent,
                    'cdate': comment.cdate.strftime('%Y-%m-%d %H:%M')
                }
            })
        except Exception as e:
            return JsonResponse({'result': 'error', 'message': str(e)})
    
    return JsonResponse({'result': 'error', 'message': 'POST 요청만 가능합니다.'})

@csrf_exempt
def delete(request):
    if request.method == 'POST':
        cno = request.POST.get('cno')
        cpw = request.POST.get('cpw', '')
        
        try:
            comment = Comment.objects.get(cno=cno)
            
            # 로그인한 사용자의 댓글인 경우
            if comment.member:
                if request.session.get('session_id') == comment.member.id:
                    comment.delete()
                    return JsonResponse({'result': 'success'})
                else:
                    return JsonResponse({'result': 'error', 'message': '삭제 권한이 없습니다.'})
            else:
                # 비회원 댓글인 경우 비밀번호 확인
                if comment.cpw == cpw:
                    comment.delete()
                    return JsonResponse({'result': 'success'})
                else:
                    return JsonResponse({'result': 'error', 'message': '비밀번호가 일치하지 않습니다.'})
        except Exception as e:
            return JsonResponse({'result': 'error', 'message': str(e)})
    
    return JsonResponse({'result': 'error', 'message': 'POST 요청만 가능합니다.'})
