from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('check-id/', views.check_id, name='check_id'),
    path('find-id/', views.find_id, name='find_id'),
    path('find-pw/', views.find_pw, name='find_pw'),
    
    path('profile/auth/', views.profile_auth, name='profile_auth'),
    path('profile/', views.profile, name='profile'),
]


