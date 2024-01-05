from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "auth_app/index.html")


# Handles user registration process
def register_page(request):
    if request.method == "POST":
        # Proccess the registration if the request is POST
        form = UserCreationForm(request.POST)
        # Check if the form is properly filled out
        if form.is_valid():
            # Creates the user
            form.save()
            # Redirect user back again to login page after successful registration
            return render(request, "auth_app/registered.html")
    else:
        # Display an empty registration form for other requests
        form = UserCreationForm()

    # Render the registration page
    return render(request, "auth_app/register.html", {"form": form})


@csrf_exempt
def user_login(request):
    # Checks if the request is POST
    if request.method == "POST":
        # Create authentication form with the submitted credentials
        form = AuthenticationForm(request, data=request.POST)

        # Check if the form is properly filled out
        if form.is_valid():
            # Get hte authenticated user from the form
            user = form.get_user()
            # login the user
            login(request, user)
            # Once logged in, redirect the user to the homepage
            return redirect("homepage")
    else:
        # Display empty reg form for other requests
        form = AuthenticationForm(request)
    # Render the registration page
    return render(request, "auth_app/login.html", {"form": form})


# Renders the homepage.html from auth_app
def homepage(request):
    username = request.user.username
    return render(request, "auth_app/homepage.html", {"username": username})


# Handles the protected view for authenticated user, if not authenticated birngs the user to the login page
@login_required(login_url="/login/")
def protected_view(request):
    return render(request, "auth_app/protected.html")
