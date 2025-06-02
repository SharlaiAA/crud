from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import templates


def web1(request):
    return render(request, 'site1.html')


def home(request):
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
        return render(request, 'home.html', {})


def login_user(request):
    pass


def logout_user(request):
    pass