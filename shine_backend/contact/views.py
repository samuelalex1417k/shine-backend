from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .models import ContactMessage
from .serializers import ContactMessageSerializer
from .utils import send_email


class ContactMessageView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)

        if serializer.is_valid():
            contact = serializer.save()

            # Send email to admin
            send_email(
    "samuelalemseged185@gmail.com",
    f"New Contact Message from {contact.name}",
    f"""
    <p><strong>Name:</strong> {contact.name}</p>
    <p><strong>Email:</strong> {contact.email}</p>
    <p><strong>Message:</strong><br>{contact.message}</p>
    """
)

            return Response({"message": "Message sent successfully"}, status=201)

        return Response(serializer.errors, status=400)
