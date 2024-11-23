from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

# Create your views here.


def index_view(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        phoneNum = request.POST['phoneNum']
        password = request.POST['password']
        user = authenticate(request, username = phoneNum, password = password)
        if user is not None:
            login(request, user)
            return redirect('account_view')
        else:
            return HttpResponse('Неверные данные для входа')


    return render(request, 'login.html')


def reg_view(request):
    if request.method == 'POST':
        fioUser = request.POST['fioUser']
        password = request.POST['password'].strip()
        phoneNum = request.POST['phoneNum']
        passwordConfirm = request.POST['passwordConfirm'].strip()
        if password != passwordConfirm:
            return HttpResponse('Пароли не совпадают')
        if User.objects.filter(username = fioUser).exists():
            return HttpResponse('Пользователь уже существует')
        
        User.objects.create(
                username = phoneNum,
                password = make_password(password),
                first_name = fioUser,
            )
        
        return redirect('login_view')

    return render(request, 'reg.html')


def resume_view(request):

    return render(request, 'resume.html')


@login_required
def account_view(request):
    

    return render(request, 'account.html')