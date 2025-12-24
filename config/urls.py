# config/urls.py
from django.contrib import admin
from django.urls import path, include  # 'include' eklemeyi unutma!

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # tracker uygulamasının url'lerini ana projeye dahil et
    path('', include('tracker.urls')),
]