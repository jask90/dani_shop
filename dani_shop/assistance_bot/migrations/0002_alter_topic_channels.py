# Generated by Django 3.2 on 2021-10-15 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistance_bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='channels',
            field=models.ManyToManyField(blank=True, to='assistance_bot.Channel', verbose_name='canales'),
        ),
    ]
