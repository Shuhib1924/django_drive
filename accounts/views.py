from django.shortcuts import render, get_object_or_404
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse(f'user {user} is still registered')
        else:
            return HttpResponse(f'User is not foundable')
    else:
        login_form = LoginForm()
    return render(request, 'registration/login.html', {'form': login_form})


def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')
    # return HttpResponse(f'you are logged out')


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = form.save(commit=False)
            new_user.set_password(cd['password'])
            new_user.save()
            return render(request, 'registration/registration_done.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {"user_form": form})


def profile(request):  # unsafe, have to be deleted later inshaAllah
    # profile = Profile.objects.get(user__username=username)
    user = get_object_or_404(User, username=request.user)
    profile = get_object_or_404(Profile, user__username=request.user)
    if request.method == "POST":
        print('\n', request.POST, '\n')
        print('\n', request.user, '\n')
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            profile = get_object_or_404(Profile, user__username=request.user)
            messages.success(request, 'your profile has been updated')
        else:
            messages.error(request, 'something gone wrong, nothing changed')
    else:
        user_form = UserEditForm(initial=model_to_dict(user))
        profile_form = ProfileEditForm(initial=model_to_dict(profile))
    context = {
        'profile': profile,
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'registration/profile.html', context)
