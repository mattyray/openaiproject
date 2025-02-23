# django_project/urls.py
from django.contrib import admin
from django.urls import path, include
from accounts.views import custom_logout  # Import the custom logout view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/logout/", custom_logout, name="logout"),  # Use custom_logout instead of LogoutView
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("", include("pages.urls")),
]
