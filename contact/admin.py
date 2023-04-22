from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'user', 'created', "status",]
    list_filter = ['status', 'phone', 'user',]
    search_fields = ['name', 'phone']
    list_per_page = 50
    list_editable = ('phone', "status", )
    ordering = ('-updated',)


admin.site.register(Contact, ContactAdmin)
