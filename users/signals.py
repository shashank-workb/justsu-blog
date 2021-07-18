from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Location
from .utils import weather


@receiver(post_save, sender=Location)
def create_profile(sender, instance, created, **kwargs):
    if created:
        city_weather = weather(instance.city)
        instance.temp = city_weather['temp']
        instance.desc = city_weather['desc']
        instance.icon = city_weather['icon']
        instance.save()