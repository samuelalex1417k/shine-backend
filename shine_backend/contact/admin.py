from django.contrib import admin
from django.core.mail import send_mail
from .models import ContactMessage


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
            send_mail(
                subject="Response from Shine LLC",
                message=f"""
Hi {obj.name},

Thank you for contacting Shine LLC.

Here is our response:

{obj.admin_reply}

Best regards,
Shine LLC Team
                """,
                from_email=None,
                recipient_list=[obj.email],
                fail_silently=False,
            )

            obj.replied = True

        super().save_model(request, obj, form, change)
