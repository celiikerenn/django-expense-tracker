from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.db.models import Sum
from django.contrib import messages

# 1. Dashboard (Ana Sayfa)
@login_required(login_url='login')
def index(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date', '-created_at')
    total_expense = transactions.aggregate(Sum('amount'))['amount__sum'] or 0
    
    chart_data = Transaction.objects.filter(user=request.user).values('category__name').annotate(total=Sum('amount'))
    labels = [item['category__name'].capitalize() for item in chart_data]
    values = [float(item['total']) for item in chart_data]

    context = {
        'transactions': transactions,
        'total_expense': total_expense,
        'labels': labels,
        'values': values,
    }
    return render(request, 'index.html', context)

# 2. Yeni İşlem Ekleme
@login_required(login_url='login')
def add_transaction(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name').strip().lower()
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        date = request.POST.get('date')

        if not category_name or not amount or not date:
            messages.error(request, 'Please fill all required fields!')
            return redirect('index')

        category, created = Category.objects.get_or_create(name=category_name)

        Transaction.objects.create(
            user=request.user,
            category=category,
            amount=amount,
            description=description,
            date=date
        )
        messages.success(request, 'Transaction added successfully!')
        return redirect('index')
    return redirect('index')

# 3. İşlem Güncelleme
@login_required(login_url='login')
def update_transaction(request, id):
    transaction = get_object_or_404(Transaction, id=id, user=request.user)

    if request.method == 'POST':
        category_name = request.POST.get('category_name').strip().lower()
        category, created = Category.objects.get_or_create(name=category_name)

        transaction.category = category
        transaction.amount = request.POST.get('amount')
        transaction.description = request.POST.get('description')
        transaction.date = request.POST.get('date')
        transaction.save()
        messages.success(request, 'Transaction updated successfully!')
        return redirect('index')

    return render(request, 'edit.html', {'transaction': transaction})

# 4. İşlem Silme
@login_required(login_url='login')
def delete_transaction(request, id):
    transaction = get_object_or_404(Transaction, id=id, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        messages.success(request, 'Transaction deleted successfully!')
    return redirect('index')

# --- AUTHENTICATION ---

def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome!')
            return redirect('index')
        else:
            # Form hatalarını göster
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password!')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('login')