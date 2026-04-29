from django.urls import path,include
from . import views

app_name='board'
urlpatterns = [
    path('list/', views.blist, name='list'),
    path('write/', views.write, name='write'),
    path('view/<int:bno>/', views.view, name='view'),
    path('update/<int:bno>/', views.update, name='update'),
    path('delete/<int:bno>/', views.delete, name='delete'),
    path('comment/<int:bno>/', views.comment_write, name='comment_write'),
    path('comment/delete/<int:cno>/<int:bno>/', views.comment_delete, name='comment_delete'),
    path('reply/<int:bno>/', views.reply, name='reply'),
]
