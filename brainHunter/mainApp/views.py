from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .models import Vacancy

# Create your views here.


def index_view(request):
    vacancy = Vacancy.objects.all()[:10]

    return render(request, 'index.html', {'vacancy': vacancy})


def vacancy_search_view(request):
    if request.GET.get('searched'):
        searched = request.GET.get('searched').lower()
        searched_city = request.GET['city'].lower()
        searched_salary = request.GET['salary']
        try:
            searched_salary = float(searched_salary)
        except ValueError:
            searched_salary = 0
        vacancy_search = Vacancy.objects.filter(title__icontains=searched, location__icontains=searched_city, salary__gte=searched_salary)
        return render(request, 'job-search.html', {
            'vacancy_search': vacancy_search,
            'searched': searched,
            'searched_city': searched_city,
            'searched_salary': searched_salary,
            })
    else:
        vacancy_search = Vacancy.objects.all()
        return render(request, 'job-search.html', {
            'vacancy_search': vacancy_search,
            })



def login_view(request):
    if request.user.is_authenticated:
        return redirect('account_view')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('account_view')
        else:
            return HttpResponse('Неверные данные для входа')


    return render(request, 'login.html')


def reg_view(request):
    if request.user.is_authenticated:
        return redirect('account_view')

    if request.method == 'POST':
        username = request.POST['username']
        fioUser = request.POST['fioUser']
        password = request.POST['password'].strip()
        phoneNum = request.POST['phoneNum']
        passwordConfirm = request.POST['passwordConfirm'].strip()
        if password != passwordConfirm:
            return HttpResponse('Пароли не совпадают')
        if User.objects.filter(username = username).exists():
            return HttpResponse('Пользователь уже существует')
        
        User.objects.create(
                username = username,
                email = phoneNum,
                password = make_password(password),
                first_name = fioUser,
            )
        
        return redirect('login_view')

    return render(request, 'reg.html')


def resume_view(request):

    return render(request, 'resume.html')


@login_required
def account_view(request):
    

    return render(request, 'acc.html')