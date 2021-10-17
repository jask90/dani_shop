from django.contrib import admin
from register_bot.models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'country',]
    ordering = ['user', 'phone', 'country',]
    search_fields = ['name', 'phone', 'country',]


admin.site.register(Profile, ProfileAdmin)
