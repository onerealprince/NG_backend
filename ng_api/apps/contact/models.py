from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

Service_CHOICES = [
    ('IT Consultation', 'IT Consultation'),
    ('Agriculture', 'Agriculture'),
    ('Facilities Management', 'Facilities Management'),
    ('Other', 'Other'),
]
class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(
        region='GH',  # Default country code (Ghana); change as needed
        blank=True,
        help_text="Enter a valid phone number with country code. Example: +233241234567")
    service = models.CharField(
        max_length=50,
        choices=Service_CHOICES,
        default='Other'
    )
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
