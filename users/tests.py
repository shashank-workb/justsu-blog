from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
# Create your tests here.
class ProfileTest(TestCase):
    def create_profile(self):
        user = User.objects.create(username='AnotherUser')
        new = SimpleUploadedFile(name='test_image.jpg', content=open(settings.MEDIA_ROOT+'/default.jpg', 'rb').read(), content_type='image/jpeg')
        return Profile(user=user, image=new)
    
    def test_Profile_creation(self):
        P = self.create_profile()
        self.assertTrue(isinstance(P, Profile))
        self.assertEqual(P.__str__(), f'{P.user.username} Profile')