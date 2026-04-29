from django.shortcuts import render

# index 함수 : 사용자가 '/' 로 들어왔을 때 실행되는 함수
def index(request):
    # request : 브라우저가 보낸 요청 정보(유저, 방식(GET/POST) 등)

    # render(요청, 템플릿이름) → 템플릿(HTML)을 읽어서 화면에 돌려준다.
    # 여기서는 프로젝트 전체에서 'index.html'이라는 파일을 찾아서 보여준다.
    return render(request, 'index.html')