from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import Profile

class TestViews(TestCase):
            

    def test_profile_detail_view_GET(self):
        Profile.objects.create(pk= 100, name = "Lucky", email ="lucky@gmail.com")
        data = {'name': 'Lucky', 'email': 'lucky@gmail.com'}
        client = Client()
        response = client.get(reverse('profile_detail', kwargs={'pk': 100}), data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
    
    def test_profile_detail_view_PUT(self):
        Profile.objects.create (pk= 1, name = "FirstName", email ="firstname@gmail.com")
        client = Client()
        data = {'name': 'NameTest', 'email': 'emailtest@gmail.com'}
        response = client.put(reverse('profile_detail', kwargs={'pk': 1}), data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        updated_profile = Profile.objects.get(pk=1)
        self.assertEqual(updated_profile.name, 'NameTest')
        self.assertEqual(updated_profile.email, 'emailtest@gmail.com')

    def test_profile_detail_view_DELETE(self):
        Profile.objects.create (pk= 2, name = "NameDeletion", email ="deleted@gmail.com")
        client = Client()
        data = {'name': 'NameDeletion', 'email': 'deleted@gmail.com'}
        response = client.delete(reverse('profile_detail', kwargs={'pk': 2}))
        
        self.assertEqual(response.status_code, 200)


        

