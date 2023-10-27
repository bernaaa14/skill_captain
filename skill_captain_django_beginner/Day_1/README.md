# Django_Beginner_Day1

## Task 1: Create Python Virtual Environment
~/Documents/SkillCaptain/skill_captain/skill_captain_django_beginner$ python3 -m venv env



## Task 2: Activate Virtual Environment
/skill_captain_django_beginner$ source env/bin/activate


## Task 3: Create Django Project
/skill_captain_django_beginner$ django-admin startproject mysite


## Task 4: Create App "myapp" and Add to INSTALLED_APPS
/skill_captain_django_beginner/mysite$ python manage.py startapp myapp

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]

## Task 5: Manually Create Static Folder Structure
/skill_captain_django_beginner/mysite$ mkdir static

## Task 6: Run Development Server
/skill_captain_django_beginner/mysite$ python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).


## Task 7: Access the Project
Open your web browser and enter the following URL: http://localhost:8000/


