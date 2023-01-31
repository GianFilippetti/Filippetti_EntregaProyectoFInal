from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile' , verbose_name='Nombre de usuario')
    phone = models.CharField(max_length=25, null=True, blank=True , verbose_name='Telefono')
    birth_date = models.DateField(null=True, blank=True , verbose_name='Fecha de nacimiento')
    profile_picture = models.ImageField(upload_to='profile_images', null=True, blank=True)


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'