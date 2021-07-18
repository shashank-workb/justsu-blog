from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Location
from .utils import get_location

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    location = forms.CharField(initial=get_location())

    class Meta:
        model = User # model that is being affected is this model, .save will save to this and next is the fields to be displayed in the order
        fields = ['username', 'email', 'password1', 'password2', 'location']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class LocationUpdateForm(forms.ModelForm):
    city = forms.CharField()
    class Meta:
        model = Location
        fields = ['city']
