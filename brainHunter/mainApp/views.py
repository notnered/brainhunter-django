from django.shortcuts import render


# Create your views here.


def index_view(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        pass

    return render(request, 'login.html')


def reg_view(request):
    if request.method == 'POST':
        pass

    return render(request, 'reg.html')