# tracker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_transaction, name='add_transaction'),
    
    # New URL for editing. <int:id> captures the transaction ID.
    # Düzenleme için yeni URL. <int:id> işlem numarasını yakalar.
    path('update/<int:id>/', views.update_transaction, name='update_transaction'),
]