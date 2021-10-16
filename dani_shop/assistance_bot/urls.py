from django.contrib import admin
from django.urls import path, re_path
from assistance_bot.views import assistance_bot, api

urlpatterns = [
    re_path(r'assistance_bot', assistance_bot.assistance_bot, name='assistance_bot'),
    re_path(r'api/ask_question', api.ask_question),
]
