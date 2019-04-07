from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput())

    email = forms.CharField(
        min_length=6,
        max_length=50,
        widget=forms.EmailInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        username_taken = User.object.filter(username=username).exist()
        if username_taken:
            raise forms.ValidationError('El nombre de usuario ya existe')
        return username


# def clean(self):
#     data = super().clean()

#     password = data['password']

#     return data


class ProfileForm(forms.Form):
    website = forms.URLField(max_length=100, required=True)
    biography = forms.CharField(max_length=100, required=False)
    picture = forms.ImageField()
