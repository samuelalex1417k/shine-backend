from django.db import models

class DriverApplication(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=500)
    license_number = models.CharField(max_length=50 ,default="", blank=False, null=False)
    expiry_date = models.DateField()
    years_experience = models.CharField(max_length=50 ,default="", blank=False, null=False )
    vehicle_make = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    vehicle_year = models.PositiveIntegerField()
    license_file = models.FileField(upload_to="licenses/", default="", blank=False,null=False)
    insurance_file = models.FileField(upload_to="insurance_files/", default="", blank=False, null=False)
    background_consent = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} ({self.status})"
