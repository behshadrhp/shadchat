from django.contrib import admin

from chat.models import Message, UserChannel


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Monitoring User actions on admin panel.
    """

    fieldsets = (
        (("Message info"), {"fields": ("user", "send_message_to", "has_seen_been", "created",)}),
        (("Message Sent"), {"fields": ("message",)}),
    )
    
    list_display = ["user", "send_message_to", "has_seen_been", "created"]
    list_filter = ["user", "send_message_to", "has_seen_been", "created"]
    ordering = ["-created"]
    list_per_page = 10
    readonly_fields = ["user", "send_message_to", "has_seen_been", "created"]

    def has_add_permission(self, request) -> bool:
        # Permission Just for SuperUser
        return False

    def has_change_permission(self, request, obj=None):
        # Permission Just for creator
        return False

    def has_delete_permission(self, request, obj=None):
        # Permission Just for SuperUser
        return request.user.is_superuser


@admin.register(UserChannel)
class UserChannelAdmin(admin.ModelAdmin):
    """
    Monitoring User actions on admin panel.
    """

    fieldsets = (
        (("Channel info"), {"fields": ("user", "channel", "updated", "created",)}),
    )
    
    list_display = ["user", "channel", "updated", "created"]
    list_filter = ["user", "updated", "created"]
    ordering = ["-created"]
    list_per_page = 10
    readonly_fields = ["user", "channel", "updated", "created"]

    def has_add_permission(self, request) -> bool:
        # Permission Just for SuperUser
        return False

    def has_change_permission(self, request, obj=None):
        # Permission Just for creator
        return False

    def has_delete_permission(self, request, obj=None):
        # Permission Just for SuperUser
        return request.user.is_superuser
