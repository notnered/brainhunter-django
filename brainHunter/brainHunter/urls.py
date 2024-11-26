"""
URL configuration for brainHunter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index_view, name='index_view'),
    path('login/', views.login_view, name='login_view'),
    path('reg/', views.reg_view, name='reg_view'),
    path('account/', views.account_view, name='account_view'),
    path('resume/<int:id>', views.resume_view, name='resume_view'),
    path('vacancy/', views.vacancy_search_view, name='vacancy_search'),
    path('create-vacancy/', views.create_vacancy_view, name='creating_vacancy'),
    path('all-vacancy/', views.all_vacancy_view, name='all_vacancy'),
    path('logout/', views.logout_view, name='logout_view'),
    path('edit-vacancy/<int:id>', views.edit_vacancy, name='edit_vacancy'),
    path('delete-vacancy/<int:id>', views.delete_vacancy, name='delete_vacancy'),
    path('create-resume/<int:id>', views.create_resume_view, name='create_resume'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)