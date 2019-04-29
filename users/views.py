from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.forms import ProfileForm, SignUpForm
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.urls import reverse


class UserDetailView(DetailView):
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(CLASS_NAME, self).get_context_data(**kwargs)
        return context


@login_required
def update_profile(request):

    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)            
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.picture = data['picture']
            profile.biography = data['biography']
            profile.save()     

            url = reverse('users:detail', kwargs={'username': request.user.username})

            return redirect(url)

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'La contraseña o el usuario no coinciden'})

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')
    

def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"]
                ))
            return redirect('posts:feed')
    else:
        form = SignUpForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )




