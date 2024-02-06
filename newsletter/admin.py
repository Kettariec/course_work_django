from django.contrib import admin
from newsletter.models import Client, Message, NewsLetter


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'comment', 'user',)
    list_filter = ('user',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'text',)
    list_filter = ('user',)


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'periodicity',)
    list_filter = ('user',)
