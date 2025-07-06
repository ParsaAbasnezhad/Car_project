from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, logout


def login_page(request):
    if request.user.is_authenticated:
        return redirect('Services:car')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Services:car')
            else:
                form.add_error(None, 'username or password is incorrect')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('Services:car')


def register_page(request):
    context = {'error':[]}
    if request.user.is_authenticated:
        return redirect('Services:car')
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            context['error'].append('passwords do not match')
            return render(request,'account/register.html',context)
        if User.objects.filter(email=email).exists():
            context['error'].append('email is already registered')
            return render(request,'account/register.html',context)
        if User.objects.filter(username=username).exists():
            context['error'].append('username is already registered')
            return render(request,'account/register.html',context)
        user = User.objects.create_user(username=username, email=email, password=password1)
        if user is not None:
            login(request, user)
            return redirect('Services:car')
        else:
            context['error'].append('username or password is incorrect')
            return render(request,'account/register.html',context)

    return render(request,'services/index.html')


