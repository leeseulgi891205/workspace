# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, GeneralUser, AdminUser

# --- 프록시 모델용 폼 정의 (필수) ---
class GeneralUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = GeneralUser

class GeneralUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = GeneralUser

class AdminUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = AdminUser
        fields = ("username", "nickname")

    def clean_nickname(self):
        nick = self.cleaned_data.get("nickname") or self.cleaned_data.get("username")
        # 닉네임 중복 방지: 존재하면 폼 에러로 처리
        if User.objects.filter(nickname=nick).exists():
            raise forms.ValidationError("이미 사용 중인 닉네임입니다.")
        return nick

    def save(self, commit=True):
        user = super().save(commit=False)
        # 닉네임 미입력 시 username으로 자동 설정
        if not getattr(user, "nickname", None):
            user.nickname = user.username
        # 관리자 프록시: 스태프로 지정
        user.is_staff = True
        if commit:
            user.save()
        return user

class AdminUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = AdminUser
# -------------------------------------

# 1. 일반 회원 관리
class GeneralUserAdmin(UserAdmin):
    form = GeneralUserChangeForm
    add_form = GeneralUserCreationForm

    list_display = ('username', 'real_name', 'grade', 'gender', 'child_school', 'date_joined')
    list_filter = ('grade', 'gender', 'child_school')
    search_fields = ('username', 'real_name', 'nickname', 'phone')

    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_staff=False)

    # 수정 화면 필드
    fieldsets = (
        ('계정 정보', {'fields': ('username', 'password', 'grade')}),
        ('개인 정보', {'fields': ('real_name', 'nickname', 'jumin', 'phone', 'email', 'address')}),
        ('상세 정보', {'fields': ('gender', 'child_school', 'terms_agreed')}),
        ('권한', {'fields': ('is_active',)}),
    )

    # 추가 화면 필드 (여기에 등급, 자녀유무 등 모두 포함)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'password_2'),
        }),
        ('필수 개인 정보', {
            'classes': ('wide',),
            'fields': ('real_name', 'nickname', 'jumin', 'phone', 'email', 'address'),
        }),
        ('회원 등급 및 상세', {
            'classes': ('wide',),
            'fields': ('grade', 'gender', 'child_school', 'terms_agreed'),
        }),
    )

# 2. 관리자 관리
class AdminUserAdmin(UserAdmin):
    form = AdminUserChangeForm
    add_form = AdminUserCreationForm
    list_display = ('username', 'real_name', 'is_superuser')
    
    # 명시적으로 안전한 필드셋 정의 (모델에 존재하는 필드만 사용)
    fieldsets = (
        ('계정 정보', {'fields': ('username', 'password')}),
        ('개인 정보', {'fields': ('real_name', 'nickname', 'email')}),
        ('권한', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    # 추가 화면에서 사용할 필드 (폼 필드와 일치: password1/password2)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'nickname', 'password1', 'password2'),
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_staff=True)

admin.site.register(GeneralUser, GeneralUserAdmin)
admin.site.register(AdminUser, AdminUserAdmin)