from django.contrib import admin
from .models import Category, Transaction

# Registering models to make them visible in the Django Admin Panel
# Modelleri Django Admin Panelinde görünür yapmak için kaydediyoruz

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) # Show only name column (Sadece isim kolonunu göster)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    # Show category, amount, and date in the list view
    # Liste görünümünde kategori, miktar ve tarihi göster
    list_display = ('category', 'amount', 'date')
    
    # Add filters for date and category on the right sidebar
    # Sağ tarafa tarih ve kategori için filtreler ekle
    list_filter = ('date', 'category')