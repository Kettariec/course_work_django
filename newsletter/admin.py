from django.contrib import admin
from newsletter.models import Client, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'comment',)
    list_filter = ('name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('client', 'title', 'text',)
    list_filter = ('client',)
