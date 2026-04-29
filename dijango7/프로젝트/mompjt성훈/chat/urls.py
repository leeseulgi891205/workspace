# ═══════════════════════════════════════════════════════════════════════
# chat/urls.py
# ═══════════════════════════════════════════════════════════════════════

from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_lobby, name='chat_lobby'),  # 채팅 로비
    path('room/<int:room_id>/', views.chat_room, name='chat_room'),  # 채팅방
    path('room/<int:room_id>/send/', views.send_message, name='send_message'),  # 메시지 전송
    path('room/<int:room_id>/fetch/', views.fetch_messages, name='fetch_messages'),  # 메시지 조회
    path('room/<int:room_id>/leave/', views.leave_room, name='leave_room'),  # 채팅방 나가기
    
    # ★ 26-01-02 추가: 🌙 새벽 2시의 수다 (WebSocket 기반 익명 채팅)
    path('midnight/', views.midnight_chat, name='midnight_chat'),  # 새벽 채팅방 페이지
]
