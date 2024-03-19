from django import forms
from .models import ServiceRequest
# from django.forms.widgets import ClearableMultipleFileInput
class ServiceRequestForm(forms.ModelForm):
    # Additional fields
    request_type = forms.ChoiceField(choices=[
        ('repair', 'Repair'),
        ('installation', 'Installation'),
        ('maintenance', 'Maintenance'),
        # Add more choices as needed
    ])
    
    details = forms.CharField(widget=forms.Textarea)

    # attached_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    attached_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}), required=False)


    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'subject', 'details', 'attached_files']