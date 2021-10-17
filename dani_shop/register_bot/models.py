from django.db import models
from django.contrib.auth.models import User


__all__ = ['Profile',]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'Teléfono')
    country = models.CharField(max_length=124, blank=True, null=True, verbose_name=u'País')


    class Meta:
        ordering = ['user']
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return f'{self.user.username}'
