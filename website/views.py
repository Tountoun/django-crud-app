from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, EmployeeForm
from .models import Employee
from django.contrib.auth.decorators import login_required


def home(request):
    employees = Employee.objects.all()
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
    context = {
        'employees': employees
    }
    return render(request, 'home.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logout successfully')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.info(request, "You have been successfully registered! Welcome")
            return redirect('home')
        return render(request, 'register.html', {'form': form})
    form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


@login_required(login_url="home")
def add_employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'employee.html', {'form': form})
    context = {
        'form': form
    }
    return render(request, 'employee.html', context)
