# config/urls.py
from django.contrib import admin
from django.urls import path, include
from tracker.views import create_admin_account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('setup-admin/', create_admin_account),
    path('', include('tracker.urls')),
]