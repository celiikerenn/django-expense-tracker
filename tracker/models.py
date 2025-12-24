from django.db import models
from django.utils import timezone

# Table for expense categories (e.g., Food, Transport, Utilities)
# Harcama kategorileri için tablo (Örn: Yemek, Ulaşım, Faturalar)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) # Name of the category (Kategori adı)

    def __str__(self):
        return self.name  # Returns the name in admin panel (Admin panelinde ismi gösterir)

# Table for actual transactions
# Gerçekleşen harcamalar için tablo
class Transaction(models.Model):
    # Relational Database Link: Each transaction belongs to a Category
    # İlişkisel Veritabanı Bağlantısı: Her harcama bir kategoriye aittir (Foreign Key)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    amount = models.DecimalField(max_digits=10, decimal_places=2) # Money amount (Para miktarı)
    description = models.TextField(blank=True, null=True) # Optional description (Opsiyonel açıklama)
    date = models.DateField(default=timezone.now) # Date of transaction (İşlem tarihi)
    created_at = models.DateTimeField(auto_now_add=True) # Record creation timestamp (Kayıt oluşturulma zamanı)

    def __str__(self):
        # Returns generic description like "Food - 100.00"
        # "Yemek - 100.00" gibi genel bir tanım döndürür
        return f"{self.category.name} - {self.amount}"