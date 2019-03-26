from django import forms


class ProfileForm(forms.Form):
    website = forms.URLField(max_length=100, required=True)
    biography = forms.CharField(max_length=100, required=False)
    picture = forms.ImageField()
