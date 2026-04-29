from django.contrib import admin
from .models import ChatRoom, ChatMessage, ChatRoomMember, MidnightChatRoom, MidnightChatMessage

# ═══════════════════════════════════════════════════════════════════════
# chat/admin.py
# 맘스로그 프로젝트 - 실시간 채팅 관리자 패널
# ═══════════════════════════════════════════════════════════════════════
# 작성일: 2026-01-02
# 기능: 채팅방, 메시지, 멤버 관리자 등록
# ═══════════════════════════════════════════════════════════════════════


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'creator', 'get_member_count', 'created_at', 'is_active')
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    
    def get_member_count(self, obj):
        return obj.member_count()
    get_member_count.short_description = '멤버 수'


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'content_preview', 'created_at', 'is_edited')
    list_filter = ('room', 'created_at', 'is_edited')
    search_fields = ('content', 'user__username', 'room__title')
    readonly_fields = ('created_at', 'edited_at')
    
    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = '내용'


@admin.register(ChatRoomMember)
class ChatRoomMemberAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'joined_at', 'is_muted')
    list_filter = ('room', 'joined_at', 'is_muted')
    search_fields = ('room__title', 'user__username')
    readonly_fields = ('joined_at', 'last_read_at')


# ═══════════════════════════════════════════════════════════════════════
# 🌙 새벽 2시의 수다 - 익명 채팅 관리자 패널
# ═══════════════════════════════════════════════════════════════════════

@admin.register(MidnightChatRoom)
class MidnightChatRoomAdmin(admin.ModelAdmin):
    """
    새벽 2시의 수다 - 채팅방 관리
    """
    list_display = ('title', 'is_active', 'start_hour', 'end_hour', 'created_at')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('기본 정보', {
            'fields': ('title', 'description', 'is_active')
        }),
        ('운영 시간', {
            'fields': ('start_hour', 'end_hour'),
            'description': '채팅방이 활성화되는 시간 범위'
        }),
        ('메타정보', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(MidnightChatMessage)
class MidnightChatMessageAdmin(admin.ModelAdmin):
    """
    새벽 2시의 수다 - 메시지 관리
    익명 처리되므로 개별 사용자 정보는 표시 안 함
    """
    list_display = ('anonymous_nickname', 'content_preview', 'created_at')
    list_filter = ('room', 'created_at')
    search_fields = ('content', 'anonymous_nickname', 'session_id')
    readonly_fields = ('session_id', 'created_at')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('메시지 정보', {
            'fields': ('room', 'content')
        }),
        ('익명 처리', {
            'fields': ('session_id', 'anonymous_nickname'),
            'description': '사용자를 식별하기 위한 익명 정보 (실제 사용자명 노출 안 함)'
        }),
        ('메타정보', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = '메시지 내용'
