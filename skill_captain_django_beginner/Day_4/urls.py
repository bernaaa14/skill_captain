
from django.contrib import admin
from django.urls import path
from myapp.views import ProfileDetailView, ProfileView
from myapp import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', ProfileView, name='profiles'),
    path('profiles/<int:pk>', ProfileDetailView, name = 'profile_detail'),
]
