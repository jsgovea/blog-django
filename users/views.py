from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from django.db.utils import IntegrityError

# @login_required
def update_profile(request):
    return render(request, 'users/update_profile.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'La contraseña o el usuario no coinciden'})

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def signup(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username=username, password=password)

        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'El nombre de usuario ya existe'})

        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        login(request, user)
        return redirect('feed')

    return render(request, 'users/signup.html')




