from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from comment.models import Comment
from member.models import Member
from customer.models import Board

def colist(request):
    # list타입으로 변경을 해서 Json타입으로 변경을 해야 함.
    # objects.filter(), objects.all() -> list타입
    
    return JsonResponse()


def codelete(request):
    cno = request.POST.get('cno','')
    Comment.objects.get(cno=cno).delete()
    context = {'result':'댓글이 삭제되었습니다.'}
    return JsonResponse(context)



def cowrite(request):
    # list타입으로 변경을 해서 Json타입으로 변경을 해야 함.
    # objects.filter(), objects.all() -> list타입
    # 넘어온 데이터 확인
    id = request.session['session_id']
    member = Member.objects.get(id=id)
    bno = request.POST.get('bno','')
    board = Board.objects.get(bno=bno)
    cpw = request.POST.get('cpw','')
    ccontent = request.POST.get('ccontent','')
    print('넘어온 데이터 : ',cpw,ccontent)
    
    # DB저장 처리 - cno : 자동생성(primary key)
    qs = Comment.objects.create(cpw=cpw,ccontent=ccontent,member=member,board=board)
    
    # 응답 데이터 구성 - member__name 포함
    l_qs = list(Comment.objects.filter(cno=qs.cno).values('cno', 'ccontent', 'cdate', 'member__name'))
    print('l_qs 등록된 댓글 : ',l_qs)
    context = {'result':'댓글이 등록되었습니다.','co':l_qs}
    return JsonResponse(context)

def codelete(request):
    """댓글 삭제"""
    try:
        cno = request.POST.get('cno', '')
        cpw = request.POST.get('cpw', '')
        
        # 댓글 조회
        comment = Comment.objects.get(cno=cno)
        
        # 비밀번호가 입력된 경우에만 확인
        if cpw:  # 비밀번호가 있으면 확인
            if comment.cpw == cpw:
                comment.delete()
                context = {'result': 'success', 'message': '댓글이 삭제되었습니다.'}
            else:
                context = {'result': 'fail', 'message': '비밀번호가 일치하지 않습니다.'}
        else:  # 비밀번호가 없으면 그냥 삭제
            comment.delete()
            context = {'result': 'success', 'message': '댓글이 삭제되었습니다.'}
        
        return JsonResponse(context)
    except Comment.DoesNotExist:
        return JsonResponse({'result': 'fail', 'message': '댓글을 찾을 수 없습니다.'})
    except Exception as e:
        print('삭제 오류:', str(e))
        return JsonResponse({'result': 'fail', 'message': '댓글 삭제 중 오류가 발생했습니다.'})

def coupdate(request):
    """댓글 수정"""
    try:
        cno = request.POST.get('cno', '')
        cpw = request.POST.get('cpw', '')
        ccontent = request.POST.get('ccontent', '')
        
        # 댓글 조회
        comment = Comment.objects.get(cno=cno)
        
        # 비밀번호가 입력된 경우에만 확인
        if cpw:  # 비밀번호가 있으면 확인
            if comment.cpw == cpw:
                comment.ccontent = ccontent
                comment.save()
                context = {'result': 'success', 'message': '댓글이 수정되었습니다.'}
            else:
                context = {'result': 'fail', 'message': '비밀번호가 일치하지 않습니다.'}
        else:  # 비밀번호가 없으면 그냥 수정
            comment.ccontent = ccontent
            comment.save()
            context = {'result': 'success', 'message': '댓글이 수정되었습니다.'}
        
        return JsonResponse(context)
    except Comment.DoesNotExist:
        return JsonResponse({'result': 'fail', 'message': '댓글을 찾을 수 없습니다.'})
    except Exception as e:
        print('수정 오류:', str(e))
        return JsonResponse({'result': 'fail', 'message': '댓글 수정 중 오류가 발생했습니다.'})

