from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    account_number = models.CharField(max_length=20, unique=True)
    # Add other fields as needed

class ServiceRequest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=[('repair', 'Repair'), ('installation', 'Installation'), ('maintenance', 'Maintenance')])
    subject = models.CharField(max_length=200)
    details = models.TextField()
    attached_files = models.FileField(upload_to='service_request_attachments/', blank=True, null=True)
    # Other fields as needed