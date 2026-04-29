from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    path("new/", views.create, name="new"),
    path("api/reports/", views.api_reports, name="api_reports"),
    path("admin-panel/", views.admin_panel, name="admin_panel"),
    path("admin-panel/<int:pk>/status/", views.update_status, name="update_status"),
]
