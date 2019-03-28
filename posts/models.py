from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

   	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')

   	profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE, verbose_name='Perfil')

   	title = models.CharField(max_length=255, verbose_name='Título')

   	description = models.TextField(max_length=250, verbose_name='Descripción')

   	photo = models.ImageField(upload_to='posts/photo', verbose_name='Imagen')

   	created = models.DateTimeField(auto_now_add=True)

   	modified = models.DateTimeField(auto_now=True)

   	def __str__(self):
   		return '{} por @{}'.format(self.title, self.user.username)
