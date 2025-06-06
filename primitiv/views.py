from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record, Reviews
from . import templates


def web1(request):
    return render(request, 'site1.html')


def home(request):
    
    reviews = Reviews.objects.select_related('user_id').all()

    if request.method == "POST":
        user_name = request.POST['user_name']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Вы успешно вошли в аккаунт")
            return redirect('home')
        else:
            messages.success(request, 'Не получилось войти')
            return redirect('home')
    else:
        return render(request, 'home.html', {'reviews' : reviews})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, 'Вы вышли из аккаунта')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Auth after signing in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, f'Добро пожаловать, {username}')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        #Looking up a record
        record = Record.objects.get(id = pk)
        reviews = Reviews.objects.filter(user_id = pk)
        return render(request, 'record.html', {'record' : record, 'reviews' : reviews})
    else:
        messages.success(request, 'Сначала нужно зарегистрироваться')
        return redirect('home')
    
    
def delete_review(request, pk):
    review = Reviews.objects.get(id = pk)
    review.delete()
    messages.success(request, 'Запись успешно удалена')
    return redirect('home')
    
    
def add_review(request):
    if request.user.is_authenticated:
        return render(request, 'add_review.html', {})
    else: redirect('home')
    
    
def all_users(request):
    records = Record.objects.all()
    
    if request.user.is_authenticated:
        return render(request, 'all_users.html', {'records' : records})
    else: redirect('home')