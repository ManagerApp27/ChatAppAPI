from django.contrib import admin
from .models import Message


class MassageAdmin(admin.ModelAdmin):

    list_display = ["contact", 'type', 'origin', 'channel', ]
    list_filter = [ 'channel', "contact", "origin",]
    search_fields = ['channel', 'contact',]
    ordering = ('-timestamp',)
    list_per_page = 50


admin.site.register(Message, MassageAdmin)
