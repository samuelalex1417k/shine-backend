# create_superuser.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shine_backend.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Check if superuser already exists
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="shineadmin", 
        email="shineadmin@gmail.com", 
        password="shine123"
    )
    print("Superuser created!")
else:
    print("Superuser already exists.")