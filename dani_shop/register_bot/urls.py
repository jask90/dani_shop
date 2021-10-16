from django.contrib import admin
from django.urls import path, re_path
from register_bot.views import register_bot, api

urlpatterns = [
    re_path(r'register_bot', register_bot.register_bot, name='register_bot'),
    re_path(r'api/register_user', api.register_user),
]
