from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'You have log in successfully')
            return redirect('home')
        messages.error(request, 'Bad credentials')
        return redirect('home')
    return render(request, 'home.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logout successfully')
    return redirect('home')


def register_user(request):
    context = {}
    return render(request, 'register.html', context)
