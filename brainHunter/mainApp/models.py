from django.contrib.auth.models import User
from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=255, default='John Doe')
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=255, choices=[
        ("male", "Male"),
        ("female", "Female"),
        ("not set", "Not Set"),
    ], default='not set')
    location = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name="profiles", blank=True)

    def __str__(self):
        return self.user.username


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account', null=True)
    company_id = models.IntegerField()
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    company_manager = models.CharField(max_length=255)
    manager_email = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Application(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="applications")
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    cover_letter = models.TextField(blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ("pending", "Pending"),
            ("accepted", "Accepted"),
            ("rejected", "Rejected"),
        ],
        default="pending",
    )

    def __str__(self):
        return f"{self.profile.user.username} -> {self.vacancy.title}"


