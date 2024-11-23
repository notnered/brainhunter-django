from django.contrib import admin
from .models import Profile, Vacancy, Application

admin.site.register(Profile)
admin.site.register(Vacancy)
admin.site.register(Application)