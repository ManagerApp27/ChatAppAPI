from django.contrib import admin
from .models import Message, Chat


class MassageAdmin(admin.ModelAdmin):
    list_display = ["contact_id", 'type', 'origin', 'channel_id', ]
    list_filter = [ 'channel_id', "contact_id", "origin",]
    search_fields = ['channel_id', 'contact_id',]
    ordering = ('-timestamp',)
    list_per_page = 50


class ChatAdmin(admin.ModelAdmin):
    list_display = ["id", "is_group_chat" ]
    list_filter = [ 'channel_id', "contact_id",]
    search_fields = ['channel_id', 'contact_id',]
    ordering = ('-timestamp',)
    list_per_page = 50
    

admin.site.register(Message, MassageAdmin)
admin.site.register(Chat, ChatAdmin)
