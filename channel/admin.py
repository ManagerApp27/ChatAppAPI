from django.contrib import admin
from .models import Channel, WhatsAppTokens


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('phone', 'name', 'status', 'user_id')
    search_fields = ('phone', 'name', 'status', 'user_id')
    list_filter = ('phone', 'name', 'status', 'user_id')
    list_editable = ('name', 'status', )
    list_per_page = 25
  

class WhatsAppTokensAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_filter = ['name']
    list_per_page = 25


admin.site.register(Channel, ChannelAdmin)
admin.site.register(WhatsAppTokens, WhatsAppTokensAdmin)