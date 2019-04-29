from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class SignUpForm(forms.Form):
    username = forms.CharField(
        min_length=4,
        max_length=50,
        label='Usuario',
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(
        max_length=70,
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    email = forms.CharField(
        min_length=6,
        max_length=50,
        label='Correo',
        widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('El nombre de usuario ya existe')
        return username

    def clean(self):
        data = super().clean()
        return data

    def save(self):
        data = self.cleaned_data

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


# def clean(self):
#     data = super().clean()

#     password = data['password']

#     return data


class ProfileForm(forms.Form):
    website = forms.URLField(max_length=100, required=True)
    biography = forms.CharField(max_length=180, required=False)
    picture = forms.ImageField()
