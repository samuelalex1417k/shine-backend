from django.contrib import admin
from .models import DriverApplication
from django.core.mail import send_mail
from django.conf import settings


@admin.register(DriverApplication)
class DriverApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "status")
    list_filter = ("status",)
    # Remove status from readonly_fields so it is editable
    # readonly_fields = ("status",)  

    def save_model(self, request, obj, form, change):
        if change:
        # Get old version BEFORE saving
            old_obj = DriverApplication.objects.get(pk=obj.pk)
            old_status = old_obj.status
        else:
            old_status = None

        # Save first
        super().save_model(request, obj, form, change)

        # Only send if status actually changed
        if change:
            new_status = obj.status

            if old_status != new_status and new_status in ["approved", "rejected"]:
                subject = f"Your Driver Application is {new_status.capitalize()}"

                if new_status == "approved":
                    message = f"""
Hi {obj.full_name},

Congratulations! Your driver application has been approved. Welcome aboard Shine LLC!

Best,
Shine LLC Team
"""
            else:
                message = f"""
Hi {obj.full_name},

We are sorry to inform you that your driver application has been rejected.

Best,
Shine LLC Team
"""

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [obj.email],
                fail_silently=False,
            )


            


        super().save_model(request, obj, form, change)
