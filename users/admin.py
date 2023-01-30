from django.contrib import admin

from users.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "username", "is_staff"]
    search_fields = ["username", "email"]
    ordering = ["email"]
    list_display_links = ["id", "email", "username"]
    exclude = ['first_name', 'last_name']
    readonly_fields = ["last_login", "date_joined"]
    actions = ['make_inactive', 'make_active']

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

