from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_of_creation',
                    'is_published', 'views_count',)
    list_filter = ('user', 'date_of_creation',)
