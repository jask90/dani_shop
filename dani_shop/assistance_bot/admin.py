from django.contrib import admin
from assistance_bot.models import *


class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name', 'function',]
    ordering = ['name',]
    search_fields = ['name',]


class TopicAdmin(admin.ModelAdmin):
    list_display = ['name',]
    ordering = ['name',]
    list_filter = ['channels',]
    search_fields = ['name',]


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Topic, TopicAdmin)
