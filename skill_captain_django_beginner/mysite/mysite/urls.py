
from django.contrib import admin
from django.urls import path
from myapp.views import GetProfile, ProfileView, UpdateEmail
from myapp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('name/', ProfileView, name='profile'),
    path('profile/<str:name>/', GetProfile,name='get_profile'),
    path('profile/<str:name>/email/',UpdateEmail,name = 'update_email'),
]
