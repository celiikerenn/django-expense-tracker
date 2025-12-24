from django.shortcuts import render, redirect, get_object_or_404 # get_object_or_404 ekle
from .models import Transaction, Category

# Main page view (Ana sayfa görünümü)
def index(request):
    # Fetch all transactions from DB, newest first
    # Tüm harcamaları veritabanından çek (en yeni en başta)
    transactions = Transaction.objects.all().order_by('-date', '-created_at')
    
    # Fetch all categories for the dropdown menu
    # Açılır menü için tüm kategorileri çek
    categories = Category.objects.all()
    
    # Calculate total expense
    # Toplam harcamayı hesapla
    total_expense = sum(t.amount for t in transactions)

    context = {
        'transactions': transactions,
        'categories': categories,
        'total_expense': total_expense
    }
    return render(request, 'index.html', context)

# Function to handle adding new transactions
# Yeni harcama ekleme işlemini yapan fonksiyon
def add_transaction(request):
    if request.method == 'POST':
        # Get data from form
        # Formdan gelen verileri al (artık 'category_name' alıyoruz)
        category_name = request.POST.get('category_name') 
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        date = request.POST.get('date')

        # CRITICAL STEP: Get the category if exists, OR create it automatically
        # KRİTİK ADIM: Kategori veritabanında varsa getir, yoksa yeni yarat.
        # .lower() kullanarak "Food" ve "food" karışıklığını önlüyoruz.
        category, created = Category.objects.get_or_create(name=category_name.lower())

        # Create the transaction linked to that category
        # Harcamayı o kategoriye bağlayarak oluştur
        Transaction.objects.create(
            category=category,
            amount=amount,
            description=description,
            date=date
        )
        
        return redirect('index')
    
def update_transaction(request, id):
    # Fetch the specific transaction or show 404 error
    # İlgili işlemi çek, yoksa hata ver
    transaction = get_object_or_404(Transaction, id=id)

    if request.method == 'POST':
        # Get updated data from form
        # Formdan güncel verileri al
        category_name = request.POST.get('category_name')
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        date = request.POST.get('date')

        # Get or create the new category (if user changed it)
        # Kategori değiştiyse bul veya oluştur
        category, created = Category.objects.get_or_create(name=category_name.lower())

        # Update fields
        # Alanları güncelle
        transaction.category = category
        transaction.amount = amount
        transaction.description = description
        transaction.date = date
        
        # Save changes to DB
        # Değişiklikleri kaydet
        transaction.save()

        # Redirect to homepage
        return redirect('index')

    # If GET request, show the edit page with existing data
    # Eğer GET isteğiyse, mevcut verilerle düzenleme sayfasını göster
    return render(request, 'edit.html', {'transaction': transaction})