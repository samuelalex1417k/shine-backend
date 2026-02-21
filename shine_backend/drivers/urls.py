from django.urls import path
from .views import DriverApplicationCreateView

urlpatterns = [
    path("apply/", DriverApplicationCreateView.as_view(), name="driver-apply"),
]
