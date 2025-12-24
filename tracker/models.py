from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # User modelini ekledik

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    # Hangi kullanıcıya ait olduğunu tutan alan:
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.category.name} - {self.amount}"