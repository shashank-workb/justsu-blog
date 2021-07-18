import requests
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, LocationUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .models import Location, Profile
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import stale_location, update_location_weather


class WeatherUpdate(View, LoginRequiredMixin):
    def get(self, request):
        update_location_weather(request.user.profile.location)
        return redirect('weather')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            location_object = Location.objects.get_or_create(
                city=form.cleaned_data.get('location').upper())
            Profile.objects.create(
                user=user_instance, location=location_object[0])
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username} Please LogIn!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def weather(request):
    city_weather = {
        'city': request.user.profile.location.city,
        'temp': request.user.profile.location.temp,
        'desc': request.user.profile.location.desc,
        'icon': request.user.profile.location.icon,
        'date': request.user.profile.location.last_update
    }
    context = {'city_weather': city_weather}
    return render(request, 'users/weather.html', context)


@login_required
def profile(request, username):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            profile_object = p_form.save(commit=False)

            prev_location = profile_object.location

            profile_object.location = Location.objects.get_or_create(
                city=request.POST.get('city').upper())[0]
            profile_object.save()

            stale_location(prev_location)

            messages.success(request, f'Your account has been updated!!')
            return redirect('profile', username=username)
    else:
        context = {
            'loggedin': get_object_or_404(User, username=username),
            'user': request.user,
            'u_form': UserUpdateForm(instance=request.user),
            'p_form': ProfileUpdateForm(instance=request.user.profile),
            'l_form': LocationUpdateForm(instance=request.user.profile.location)
        }

    return render(request, 'users/profile.html', context)


class Logincustom(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('blog-home'))
        return super(LoginView, self).get(request, *args, **kwargs)
