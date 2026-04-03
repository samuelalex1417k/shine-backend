from django.contrib import admin
from django.core.mail import send_mail
from .models import ContactMessage
from .utils import send_email


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at", "replied")
    list_filter = ("replied", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("name", "email", "phone", "message", "created_at")

    fieldsets = (
        ("User Information", {
            "fields": ("name", "email", "phone", "message", "created_at")
        }),
        ("Admin Response", {
            "fields": ("admin_reply", "replied")
        }),
    )

    def save_model(self, request, obj, form, change):
        # If admin wrote a reply and hasn't replied before
        if obj.admin_reply and not obj.replied:
            send_email(
            obj.email,
        "Response from Shine LLC",
        f"""
        <p>Hi {obj.name},</p>
        <p>{obj.admin_reply}</p>
        <p>– Shine LLC</p>
        """
        )

        obj.replied = True

        super().save_model(request, obj, form, change)
