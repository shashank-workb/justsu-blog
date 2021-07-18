from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone

class Location(models.Model):
    city = models.CharField(primary_key=True, max_length=100, default='LONDON')
    temp = models.CharField(max_length=10, null=True)
    desc = models.CharField(max_length=100, default='Weather Report Not Available')
    icon = models.CharField(max_length=200, default='04d')
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.city}'
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, commit=True, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img = img.convert('RGB')
            img.save(self.image.path)