from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            profile = profile_form.save(commit=False)
            profile.user_id = User.objects.get(username=username).id
            profile.save()
            messages.success(
                request, f'Hi {username}! Your account has been created successfully. You can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
        profile_form = ProfileUpdateForm()
    return render(request, 'user/register.html', {'form': form, 'profile_form': profile_form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(
                request, f'Hi {username}! Your profile has been updated successfully.')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'user/profile.html', {'user_form': user_form, 'profile_form': profile_form})
