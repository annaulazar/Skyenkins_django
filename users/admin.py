from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "username", "role"]
    search_fields = ["username", "email"]
    ordering = ["email"]
    list_display_links = ["id", "email", "username"]
    actions = ['make_inactive', 'make_active']
    fields = ['email', 'username', 'password', 'role']

    @admin.action(description='Сделать выбранных пользователей не активными')
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    @admin.action(description='Сделать выбранных пользователей активными')
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.set_password(obj.password)
        obj.username = obj.username.lower()
        obj.save()

