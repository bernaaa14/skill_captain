from myapp.models import Profile
from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

@csrf_exempt
def ProfileView(request):
    """
    Description:
    Creates a new profile with the provided information.
    Get the list of profiles already created.

    Parameters:

    POST: 
    name (str): The name of the profile.
    email (str): The email address of the profile.

    GET: None
    """

    if request.method == 'GET':
        profiles = Profile.objects.all()
        data = [{'id': profile.id, 'name': profile.name, 'email': profile.email} for profile in profiles]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        # Parse JSON data from the request
        json_data = json.loads(request.body.decode('utf-8'))
        name = json_data.get('name')
        email = json_data.get('email')
        mobile_number = json_data('mobile_number')
        address = json_data.get('address')
        # Create and save the profile
        profile = Profile(name=name, email=email, age = age, occupation = occupation, mobile_number= mobile_number, address = address)
        #checks if name and email is missing in the post request
        if not name or not email:
            return JsonResponse({'message': 'Missing fields!'} )
        profile.save()

        # Return the saved profile in the API response
        serialized_obj = serializers.serialize('json', [profile, ])
        data = json.loads(serialized_obj)
        return JsonResponse({'message': 'Profile created successfully', 'data': data[0]})
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def ProfileDetailView(request, pk):
    """    
    Description:
    Perform operations on the user profile based on the specified primary key

    Args:
        request (HttpRequest): HttpRequest for the API endpoint
        pk (integer): The primary key (id) for the profile

     Returns:
        JsonResponse based on the HTTP method that is used
        - Request Method: GET, retrieve the profile details
        - Request Method: PUT, update profile name and email
        - Request Method: DELETE, delete the profile
    """
    # Checks if the profile exist with the specified primary key
    try:
        profile = Profile.objects.get(id=pk)  
    except Profile.DoesNotExist:
          return HttpResponseNotFound('Profile does not exist')
    if request.method == 'GET':
        if not profile:
            return JsonResponse({'message': 'Profile does not exist'})
        data = {'id': profile.id, 'name': profile.name, 'email': profile.email}
        return JsonResponse(data)
    # Updates the name and email with associated pk in the database
    elif request.method == 'PUT':
        json_data = json.loads(request.body.decode('utf-8'))
        name = json_data.get('name')
        email = json_data.get('email')
        profile.name = name
        profile.email = email
        profile.save()
        data = {'id': profile.id, 'name': profile.name, 'email': profile.email}
        return JsonResponse(data)
    # Deletes the profile with associated pk in the database
    elif request.method == 'DELETE':
        profile.delete()
        # Display a response indicating profile deletion successful
        return JsonResponse({'message': 'Profile Deleted Successfully!'})
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)