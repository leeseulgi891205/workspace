from django.contrib import admin
from django.urls import path, include
from reports.views import main

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", main, name="main"),

    path("accounts/", include("accounts.urls")),
    path("mypage/", include("mypage.urls")),
    path("notices/", include("notices.urls")),
    path("reports/", include("reports.urls")),
    path("chatbot/", include("chatbot.urls")),
]
