from django.db import models
from django.contrib.auth.models import User  # Import User model
from customers.models import ServiceRequest

class SupportTicket(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Open')
    created_at = models.DateTimeField(auto_now_add=True)
