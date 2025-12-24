from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages

# Kullanıcı giriş yapmamışsa bu sayfayı gösterme, login'e at
@login_required(login_url='login')
def index(request):
    # Sadece giriş yapan kullanıcının (request.user) harcamalarını getir
    transactions = Transaction.objects.filter(user=request.user).order_by('-date', '-created_at')
    
    categories = Category.objects.all()
    total_expense = sum(t.amount for t in transactions)

    context = {
        'transactions': transactions,
        'categories': categories,
        'total_expense': total_expense
    }
    return render(request, 'index.html', context)

@login_required(login_url='login')
def add_transaction(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        date = request.POST.get('date')

        category, created = Category.objects.get_or_create(name=category_name.lower())

        Transaction.objects.create(
            user=request.user,  # Harcamayı yapan kişiyi kaydet
            category=category,
            amount=amount,
            description=description,
            date=date
        )
        return redirect('index')

@login_required(login_url='login')
def update_transaction(request, id):
    # Sadece kendi harcamasını düzenleyebilsin (başkası ID tahmin edip giremesin)
    transaction = get_object_or_404(Transaction, id=id, user=request.user)

    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        category, created = Category.objects.get_or_create(name=category_name.lower())

        transaction.category = category
        transaction.amount = request.POST.get('amount')
        transaction.description = request.POST.get('description')
        transaction.date = request.POST.get('date')
        transaction.save()

        return redirect('index')

    return render(request, 'edit.html', {'transaction': transaction})

# --- YENİ EKLENEN LOGIN/REGISTER FONKSİYONLARI ---

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Kayıt olunca otomatik giriş yap
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def create_superuser_view(request):
    try:
        # Eğer admin zaten varsa hata vermesin
        if not User.objects.filter(username='admin').exists():
            # Kullanıcı adı: admin, Şifre: 123456 (Bunu hemen değiştireceğiz)
            User.objects.create_superuser('admin', 'admin@example.com', '123456')
            return HttpResponse("Superuser created! <br>User: admin <br>Pass: 123456")
        else:
            return HttpResponse("The admin user already exists.")
    except Exception as e:
        return HttpResponse(f"Hata oluştu: {e}")
    
    # tracker/views.py içine ekle

@login_required(login_url='login')
def delete_transaction(request, id):
    # Sadece o kullanıcıya ait işlemi bul, yoksa hata ver
    transaction = get_object_or_404(Transaction, id=id, user=request.user)
    
    if request.method == 'POST':
        transaction.delete()
        return redirect('index')
    
    # Güvenlik için GET isteğiyle silinmez, onay sayfasına veya direkt POST'a yönlendirilir
    # Biz pratik olsun diye direkt işlem yapacağız ama HTML'de form kullanacağız.
    return redirect('index')