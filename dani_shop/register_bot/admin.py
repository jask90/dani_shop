from django.contrib import admin
from register_bot.models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'origin',]
    ordering = ['user', 'phone', 'origin',]
    search_fields = ['name', 'phone',]


admin.site.register(Profile, ProfileAdmin)
