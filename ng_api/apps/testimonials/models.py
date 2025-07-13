from django.db import models

SERVICE_CHOICES = [
    ('IT Consultation', 'IT Consultation'),
    ('Agriculture', 'Agriculture'),
    ('Facilities Management', 'Facilities Management'),
    ('Other', 'Other'),
]

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default='Other')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"
