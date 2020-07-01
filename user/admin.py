from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from cms import settings
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'image')
    search_fields = ('user_id__username',)
    list_per_page = settings.LIST_PER_PAGE


admin.site.register(Profile, ProfileAdmin)

admin.AdminSite.site_header = 'Dashboard'
admin.site.unregister(Group)
# set list_per_page for builtin User class
UserAdmin.list_per_page = settings.LIST_PER_PAGE