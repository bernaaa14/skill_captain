# Task 1 : Create a view hello_world 
from django.http import HttpResponse

def hello_world(request):
     return HttpResponse("Greetings from the nth world")

# Task 2: map it to endpoint hello/
from django.urls import path
from myapp.views import hello_world

urlpatterns = [
    path('hello/', hello_world, name='bernaaa14'),
]