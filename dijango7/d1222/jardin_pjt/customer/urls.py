from django.urls import path,include
from . import views

app_name='customer'
urlpatterns = [
    # html리턴
    path('clist/', views.clist, name='clist'),
    path('cwrite/', views.cwrite, name='cwrite'),
    path('cepilog/', views.cepilog, name='cepilog'),
    path('cinquiry_write/', views.cinquiry_write, name='cinquiry_write'),
    path('cview/<int:bno>/', views.cview, name='cview'),
    # 좋아요 링크
    path('clikes/', views.clikes, name='clikes'),
    
]

