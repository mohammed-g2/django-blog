from django.urls import path
from django.contrib import admin
from django.template.response import TemplateResponse
from blog.models import Post
from cms import settings


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('date',)
    search_fields = ('title', 'author__username')
    list_per_page = settings.LIST_PER_PAGE

admin.site.register(Post, PostAdmin)
