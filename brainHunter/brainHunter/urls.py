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
    path('resume/', views.resume_view, name='resume_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)