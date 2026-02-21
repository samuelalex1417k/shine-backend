from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .models import ContactMessage
from .serializers import ContactMessageSerializer


class ContactMessageView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)

        if serializer.is_valid():
            contact = serializer.save()

            # Send email to admin
            send_mail(
                subject=f"New Contact Message from {contact.name}",
                message=f"""
Name: {contact.name}
Email: {contact.email}
Phone: {contact.phone}

Message:
{contact.message}
                """,
                from_email=None,
                recipient_list=["samuelalemseged185@gmail.com"],
                fail_silently=False,
            )

            return Response({"message": "Message sent successfully"}, status=201)

        return Response(serializer.errors, status=400)
