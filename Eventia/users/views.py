from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm
from .models import Profile


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('user_detail')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('user_detail')
        else:
            error = 'Invalid username or password'
            return render(request, 'users/login.html', {'error': error})
    return render(request, 'users/login.html')


@login_required
def user_detail_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if p_form.is_valid():
            p_form.save()
    else:
        p_form = ProfileUpdateForm(instance=profile)
    return render(request, 'users/user_detail.html', {'profile': profile, 'p_form': p_form})


def logout_view(request):
    logout(request)
    return redirect('home_page')
