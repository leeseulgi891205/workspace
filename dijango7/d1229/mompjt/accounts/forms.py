# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # models.py에 있는 필드 이름과 똑같아야 합니다!
        fields = (
            'username', 
            'real_name', 
            'nickname', 
            'jumin',
            'phone', 
            'email',
            'address', 
            'gender',       # [변경] 성별
            'child_school', # [변경] 자녀 학교
        )
    
    # 필수 입력 설정
    jumin = forms.CharField(required=True)
    email = forms.EmailField(required=True)