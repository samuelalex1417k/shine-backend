# drivers/management/commands/test_email.py
from django.core.management.base import BaseCommand
from django.core.mail import send_mail

class Command(BaseCommand):
    help = "Test sending email"

    def handle(self, *args, **kwargs):
        send_mail(
            "Test Email",
            "This is a test from Shine LLC.",
            "noreply@shine-llc.com",
            ["samuelalemseged855@gmail.com"],  # replace with actual email
            fail_silently=False,
        )
        self.stdout.write(self.style.SUCCESS("Email sent successfully!"))
