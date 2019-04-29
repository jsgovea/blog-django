from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                verbose_name='Nombre Usuario')
    website = models.URLField(max_length=100, blank=True)
    biography = models.TextField(max_length=100, blank=True,
                                 verbose_name='Acerca de mi')
    picture = models.ImageField(upload_to='users/pictures',
                                verbose_name='Foto de Perfil')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
