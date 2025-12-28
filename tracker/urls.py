from django.urls import path
from . import views
from .views import create_admin

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('update/<int:id>/', views.update_transaction, name='update_transaction'),
    path('setup-admin/', create_admin),
    
    # Yeni Authentication Linkleri
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/<int:id>/', views.delete_transaction, name='delete_transaction'),
]
