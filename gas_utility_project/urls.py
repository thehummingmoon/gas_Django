from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customers.urls')), 
    # Add more URL patterns as needed
]