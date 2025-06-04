from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
from . import templates


def web1(request):
    return render(request, 'site1.html')


def home(request):
    
    records = Record.objects.all()
    
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
        return render(request, 'home.html', {'records' : records})


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