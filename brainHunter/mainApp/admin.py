from django.contrib import admin
from .models import Profile, Vacancy, Application, Skill, Company

admin.site.register(Profile)
admin.site.register(Vacancy)
admin.site.register(Application)
admin.site.register(Skill)
admin.site.register(Company)