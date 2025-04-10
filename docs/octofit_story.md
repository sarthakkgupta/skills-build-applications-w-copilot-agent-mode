# Building a Fitness App with GitHub Copilot agent mode for Mergington High School

## OctoFit Tracker application story for Mergington High School

Paul Octo has been a physical education teacher at Mergington High School for over 8 years. Despite his enthusiasm and creative approach to gym class, he's been increasingly concerned about students' physical activity declining once they leave school grounds. Many students admitted they rarely exercised outside of the required PE classes.
After attending a professional development conference on "Technology Integration in Physical Education," Paul became inspired to create a solution. He wanted something that would:

1. Make fitness tracking fun and engaging
2. Create positive peer pressure through friendly competition
3. Allow him to monitor student progress remotely
4. Provide personalized guidance based on individual fitness levels

## The Birth of OctoFit Tracker

Paul initially sketched his idea on a notepad during lunch breaks. He envisioned an app where students could log workouts, earn achievement badges, and compete in monthly fitness challenges. However, as a PE teacher with only basic coding knowledge, the technical aspects seemed daunting.
That's when he approached Jessica Cat, the head of Mergington High's IT department. Jessica recommended basing the app on the Monafit Tracker developed by Mona High School, which was documented in `docs/mona-high-school-fitness-tracker.md`. She saw potential in adapting the Monafit Tracker's structure and features to meet Mergington High School's needs.

### Technical Planning Phase

Before starting development, Paul and Jessica carefully reviewed the Monafit Tracker's repository and documentation. This provided a solid foundation for OctoFit Tracker, ensuring compliance with technical standards and leveraging proven design patterns.
Together, Paul and the IT team identified key requirements for OctoFit Tracker:

### User Experience Goals

- Simple, intuitive interface designed specifically for teenagers
- Quick activity logging to minimize friction
- Social features that respect student privacy
- Gamification elements to maintain engagement

### Technical Specifications

- Mobile-responsive web application (accessible on school Chromebooks and personal devices)
- Secure authentication based on Monafit Tracker's implementation
- Activity verification system to prevent cheating

## Current Development Status

Paul and Jessica have set up a GitHub Codespace environment and are making remarkable progress with GitHub Copilot agent mode. By adapting the Monafit Tracker's structure, the OctoFit Tracker prototype already includes:

- A functional user registration system
- Basic activity logging for running, walking, and strength training
- The beginning framework for team competitions
- A simple dashboard showing student progress

## Next Steps for Paul

With the basic infrastructure in place, Paul is now focused on:

1. Developing an engaging point system that fairly compares different types of activities
2. Creating motivational challenges that appeal to different student interests
3. Building a notification system that encourages consistency without being intrusive
4. Designing reports that help him identify students who might need additional support or motivation

The IT department has been impressed with how GitHub Copilot agent mode has accelerated development, allowing Paul to focus on the educational aspects while the AI handles much of the technical implementation. Jessica Cat has been particularly pleased with how OctoFit Tracker leverages the Monafit Tracker's foundation to meet Mergington High School's unique requirements.

### Workshop Overview

In this workshop, you'll:

1. Set up a development environment using **GitHub Codespaces**
2. Use **GitHub Copilot** to accelerate development across multiple technologies
3. Build key components of the **OctoFit Tracker** app with the help of Copilot agent mode
4. Learn best practices and prompting techniques for working with **GitHub Copilot agent mode**

### Application Features

**OctoFit Tracker** will include:

- User profiles
- Activity logging and tracking
- Team creation and management
- A competitive leaderboard
- Personalized workout suggestions

### GitHub Copilot Chat

These are the current models supported for GitHub Copilot Chat.

- Claude Sonnet 3.5 (Preview)
- Claude Sonnet 3.7 (Preview)
- Claude Sonnet 3.7 Thinking (Preview)
- Gemini 2.0 Flash (Preview)
- GPT-4o
- o1 (Preview)
- o3-mini (Preview)

#### [LLM models explained](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat#ai-models-for-copilot-chat-1)

![GitHub Copilot Chat models](https://github.com/user-attachments/assets/f2f8d0bd-366b-4ecf-b88d-d092ae7b8b10)

#### Prompt engineering

- [GitHub documentation prompt engineering](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
- [How to use GitHub Copilot: Prompts, tips, and use cases](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)
- [Using GitHub Copilot in your IDE: Tips, tricks, and best practices](https://github.blog/2024-03-25-how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices/)
- [A developer's guide to prompt engineering and LLMs](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot#:~:text=A%20developer%E2%80%99s%20guide%20to%20prompt%20engineering%20and%20LLMs)
- [GitHub Copilot: The Agent Awakens](https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/#agent-mode-available-in-preview-%f0%9f%a4%96)

### OctoFit tracker fitness application technology stack

We'll be using a modern web application stack:

- **Frontend**: React.js
- **Backend**: Python with Django REST Framework
- **Database**: MongoDB
- **Development Environment**: GitHub Codespaces

### Workshop Structure

1. **Introduction**
   - Overview of OctoFit Tracker app concept
   - GitHub Copilot Chat models

2. **Setup of Prerequisites**
   - Setting up GitHub Codespaces
   - Ensure GitHub Copilot and Copilot Chat extensions are up to date

3. **Rapid Prototyping with GitHub Copilot agent mode**
   - Creating project structure
   - Generating boilerplate code
   - Implementing basic models, serializers, URLs, and views

4. **Building Core Features**
   - Activity logging API
   - Team management
   - Leaderboard functionality

5. **Frontend and Backend Development**
   - Setting up React components
   - Implementing responsive UI
   - Connecting to backend APIs
   - Python Django business logic
   - MongoDB data layer

### Django Settings for OctoFit Tracker

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "your-secret-key"
DEBUG = True

ALLOWED_HOSTS = ['*']  # Allow all hosts

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "djongo",
    "corsheaders",
    "octofit_tracker",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # CORS middleware first
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "octofit_tracker.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "octofit_tracker.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "octofit_db",
        "HOST": "localhost",
        "PORT": 27017,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOW_ALL_ORIGINS = True  # Allow all cross-origin requests
```

### Django Models for OctoFit Tracker

```python
from djongo import models

class User(models.Model):
    _id = models.ObjectIdField()
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, unique=True)
    members = models.ArrayReferenceField(
        to=User,
        on_delete=models.CASCADE,
        blank=True
    )

    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.DurationField()

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}: {self.score}"

class Workout(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
```

### Django Serializers for OctoFit Tracker

```python
from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    user = ObjectIdField()

    class Meta:
        model = Activity
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Leaderboard
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = Workout
        fields = '__all__'
```

### Django URLs for OctoFit Tracker

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    TeamViewSet,
    ActivityViewSet,
    LeaderboardViewSet,
    WorkoutViewSet,
    api_root
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

urlpatterns = [
    path('', api_root, name='api-root'),  # api_root endpoint
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
```

### Django Admin for OctoFit Tracker

```python
from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'duration')

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'score')

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name',)
```

### Django Tests for OctoFit Tracker

```python
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User

class BasicTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "pass1234"
        }
        # Create a user to test GET, etc.
        self.user = User.objects.create(**self.user_data)

    def test_api_root(self):
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that API endpoints are listed
        self.assertIn('users', response.data)

    def test_get_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
```
