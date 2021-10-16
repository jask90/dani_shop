from django.db import models


__all__ = ['Topic', 'Channel']


class Channel(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name=u'nombre')
    function = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'nombre de función')

    class Meta:
        ordering = ['name']
        verbose_name = 'canal'
        verbose_name_plural = 'canales'

    def __str__(self):
        return f'{self.name}'


class Topic(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name=u'nombre')
    channels = models.ManyToManyField(Channel, blank=True, verbose_name=u'canales')

    class Meta:
        ordering = ['name']
        verbose_name = 'tema'
        verbose_name_plural = 'temas'

    def __str__(self):
        return f'{self.name}'
