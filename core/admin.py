from django.contrib import admin
from django.contrib.auth.models import Group

from core.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
    exclude = ['groups', 'user_permissions', 'password', 'is_superuser']
    search_fields = ['username', 'first_name', 'last_name']
    list_filter = ['is_staff', 'is_active', 'is_superuser']
    readonly_fields = ['date_joined', 'last_login']


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
