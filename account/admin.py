# admin.py
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from account.models import User, Profile, Settings


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Monitoring User actions on admin panel.
    """

    fieldsets = (
        (("Personal info"), {"fields": ("username", "email", "password")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2",  "is_active", "is_staff", "is_superuser"),
            },
        ),
    )

    list_display = ["username", "email", "is_staff", "is_superuser", "is_active", "formatted_date_joined"]
    list_filter = ("is_staff", "is_superuser", "is_active", "date_joined")
    ordering = ["-is_superuser", "-is_staff", "-last_login"]
    list_per_page = 10
    readonly_fields = ["date_joined"]

    @admin.display(description="Date Joined")
    def formatted_date_joined(self, obj):
        return obj.date_joined.strftime("%Y-%m-%d") if obj.date_joined else None

    def has_add_permission(self, request) -> bool:
        # Permission Just for SuperUser
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        # Permission Just for creator
        return obj and obj == request.user or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        # Permission Just for SuperUser
        return request.user.is_superuser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Monitoring User profile on admin panel.
    """

    fieldsets = (
        (None, {"fields": ("avatar", "first_name", "last_name",)}),
        (("Personal info"), {"fields": ("gender", "bio")}),
    )

    list_display = ["user", "first_name", "last_name","created", "updated"]
    list_filter = ["gender", "created", "updated"]
    search_fields = ["user__username__icontains", "first_name__icontains", "last_name__icontains", "bio__icontains"]
    list_per_page = 10
    readonly_fields = ["user"]

    def has_add_permission(self, request) -> bool:
        # Permission Just for SuperUser
        return False

    def has_change_permission(self, request, obj=None):
        # Permission Just for creator
        return obj and obj == request.user or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        # Permission Just for SuperUser
        return request.user.is_superuser
    
    def get_readonly_fields(self, request, obj=None):
        # Only superusers can edit the specified fields
        if obj.user == request.user or request.user.is_superuser:
            return []
        elif request.user.is_staff:
            return ["user", "avatar", "first_name", "last_name", "bio", "created", "updated"]


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    """
    Monitoring User profile on admin panel.
    """

    fieldsets = (
        (("settings"), {"fields": ("disable", "notification",)}),
        (("Permissions"), {"fields": ("admin", "special", "writer",)}),
    )
    list_display = ["user", "admin", "special", "writer", "notification", "disable", "created", "updated"]
    list_filter = ["admin", "special", "writer", "notification", "disable", "created", "updated"]
    search_fields = ["user__username__icontains"]
    list_per_page = 10
    readonly_fields = ["user"]

    def has_add_permission(self, request) -> bool:
        # Permission Just for SuperUser
        return False

    def has_change_permission(self, request, obj=None):
        # Permission Just for creator
        return obj and obj == request.user or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        # Permission Just for SuperUser
        return request.user.is_superuser
    
    def get_readonly_fields(self, request, obj=None):
        # Only superusers can edit the specified fields
        if obj.user == request.user or request.user.is_superuser:
            return []
        elif request.user.is_staff:
            return ["user", "admin", "special", "writer", "notification", "disable", "created", "updated"]
