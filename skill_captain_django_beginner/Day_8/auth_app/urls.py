from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registration_page/", views.register_page, name="registration_page"),
    path("login/", views.user_login, name="login"),
    path("homepage/", views.homepage, name="homepage"),
    path("protected/", views.protected_view, name="protected"),
]
