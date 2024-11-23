# Generated by Django 5.1.3 on 2024-11-23 15:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('company', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('bio', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_letter', models.TextField(blank=True, null=True)),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=50)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='mainApp.profile')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='mainApp.vacancy')),
            ],
        ),
    ]
