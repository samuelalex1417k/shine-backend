from rest_framework import generics
from .models import DriverApplication
from .serializers import DriverApplicationSerializer

class DriverApplicationCreateView(generics.CreateAPIView):
    queryset = DriverApplication.objects.all()
    serializer_class = DriverApplicationSerializer
