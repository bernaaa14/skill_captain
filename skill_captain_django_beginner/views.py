from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from myapp.models import Profile
from django.http import JsonResponse
from django.http import Http404
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import json


def ProfileView(request):
     if request.method == 'POST':
          name = request.POST.get('name', '')
          age = request.POST.get('age', 0)
          occupation = request.POST.get('occupation', '')
          email = request.POST.get('email', '')
          Profile.objects.create(name=name, age=age, occupation=occupation,email=email)
          return redirect('profile')
     else:
          profiles = Profile.objects.all()
          context = {'profiles': profiles}
          return render(request, 'profile.html', context)

def GetProfile(request, name):
     try:
          # Retrieve the profile object based on the argument name
          profile = Profile.objects.get(name=name)
     except Profile.DoesNotExist:
          raise print("Profile Does not Exist")
     
     # Create dictionary containing the data of the profile
     profile_data = {
        'name': profile.name,
        'age': profile.age,
        'occupation': profile.occupation,
        'email': profile.email,
    }
     # Return the profile data
     return JsonResponse(profile_data)

def UpdateEmail(request, name):
    # Check the http request is PUT
    if request.method == 'PUT':
        try:
            # Retrive the profile object based on the argument name
            profile = Profile.objects.get(name=name)
            if request.content_type == 'application/json':
                # parse the json data to the body
                data = json.loads(request.body)
                # retrieve the email
                updated_email = data.get('email')
                # Check if email is present
                if updated_email is not None:
                    try:
                        validate_email(updated_email)  # Check if it's a valid email
                    # Raise a validation error once the email is invalid
                    except ValidationError:
                        return JsonResponse({'error': 'Invalid email address'}, status=400)
                    # Update the email of the profile with the new email
                    profile.email = updated_email
                    profile.save()
                    # Return the updated profile info
                    return JsonResponse({
                        'name': profile.name,
                        'age': profile.age,
                        'occupation': profile.occupation,
                        'email': profile.email
                    })
                return JsonResponse({'error': 'Email parameter missing'}, status=400)
            return JsonResponse({'error': 'Invalid content type'}, status=415)
        except Profile.DoesNotExist:
            raise Http404("Profile does not exist")
    return JsonResponse({'error': 'Invalid request method'}, status=405)