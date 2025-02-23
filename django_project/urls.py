# django_project/urls.py
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),  # Keep it simple
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("", include("pages.urls")),
]
