from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .models import Vacancy, Company, Profile

# Create your views here.


def index_view(request):
    vacancy = Vacancy.objects.filter(is_active=True).order_by('-posted_at')[:10]

    return render(request, 'index.html', {'vacancy': vacancy})


def vacancy_search_view(request):
    if request.GET.get('searched') or request.GET.get('city') or request.GET.get('salary'):
        searched = request.GET.get('searched').lower()
        searched_city = request.GET['city'].lower()
        searched_salary = request.GET['salary']
        try:
            searched_salary = float(searched_salary)
        except:
            searched_salary = 0
        vacancy_search = Vacancy.objects.filter(is_active=True, title__icontains=searched, location__icontains=searched_city, salary__gte=searched_salary).order_by('-posted_at')
        print('post', searched, searched_city, searched_salary)
        return render(request, 'job-search.html', {
            'vacancy_search': vacancy_search,
            'searched': searched.capitalize(),
            'searched_city': searched_city.capitalize(),
            'searched_salary': searched_salary,
            })
    else:
        vacancy_search = Vacancy.objects.filter(is_active=True).order_by('-posted_at')
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


def create_vacancy_view(request):
    if not request.user.is_staff:
        return HttpResponse('У вас недостаточно прав')
    
    company = Company.objects.get(user=request.user)
    
    if request.method == 'POST':
        vacancyTitle = request.POST['vacancyTitle']
        vacancySalary = request.POST['vacancySalary']
        vacancyLocation = request.POST['vacancyLocation']
        vacancyDesc = request.POST['vacancyDesc']
        company = Company.objects.get(user=request.user)
        Vacancy.objects.create(
            title = vacancyTitle,
            description = vacancyDesc,
            company = company,
            location = vacancyLocation,
            salary = vacancySalary,
        )

    return render(request, 'creating-vacancy.html', {'company': company})


def edit_vacancy(request, id):
    try:
        company = Company.objects.get(user=request.user)
    except:
        return HttpResponse('У вас недостаточно прав')
    vacancyObj = Vacancy.objects.get(id=id)

    if vacancyObj.company != company.name:
        return HttpResponse('У вас недостаточно прав')

    if request.method == 'POST':
        vacancyObj.title = request.POST['vacancyTitle'].lower()
        vacancyObj.salary = float(request.POST['vacancySalary'])
        vacancyObj.location = request.POST['vacancyLocation'].lower()
        vacancyObj.description = request.POST['vacancyDesc']
        vacancyObj.save()
        return redirect('all_vacancy')


    return render(request, 'edit-vacancy.html', {'vacancyObj': vacancyObj, 'company': company})


def delete_vacancy(request, id):
    try:
        company = Company.objects.get(user=request.user)
    except:
        return HttpResponse('У вас недостаточно прав')
    vacancyObj = Vacancy.objects.get(id=id)

    if vacancyObj.company != company.name:
        return HttpResponse('У вас недостаточно прав')

    if request.method == 'POST':
        vacancyObj.is_active = False
        vacancyObj.save()
        return redirect('all_vacancy')
    
    return render(request, 'delete.html', {'vacancyObj': vacancyObj, 'company': company})


def all_vacancy_view(request):
    if not request.user.is_staff:
        return HttpResponse('У вас недостаточно прав')
    
    company = Company.objects.get(user=request.user)
    myVacancy = Vacancy.objects.filter(company=company.name).order_by('-posted_at')
    

    return render(request, 'all-vacancy.html', {'company': company, 'myVacancy': myVacancy})


def resume_view(request, id):
    profile = Profile.objects.get(user_id=id)

    return render(request, 'resume.html', {'profile': profile})


def logout_view(request):
    logout(request)
    return redirect('index_view')


@login_required
def account_view(request):
    user = request.user
    try:
        userProfile = Profile.objects.get(user=user)
    except:
        return redirect('all_vacancy')

    return render(request, 'acc.html', {'userProfile': userProfile})

