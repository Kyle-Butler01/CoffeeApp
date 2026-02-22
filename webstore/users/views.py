from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required


def register_page (request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login (request, user)
            return redirect ('main:home')
    else:
        form = RegisterForm()

    return render (request, 'users/register.html', {'form':form})

@login_required
def profile_page (request):
    return render (request, 'users/profile.html')


@login_required
def edit_profile_page (request):
    if request.method == 'POST':
        profile = request.user.profile
        
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'users/edit_profile.html', {'form': form})

