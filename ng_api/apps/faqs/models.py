from django.db import models


Service_CHOICES = [
    ('IT Consultation', 'IT Consultation'),
    ('Agriculture', 'Agriculture'),
    ('Facilities Management', 'Facilities Management'),
    ('Other', 'Other'),
]

class Faqs(models.Model):
    question = models.CharField()
    answer = models.CharField()
    service = models.CharField(max_length= 50, choices= Service_CHOICES, default= 'Other')
    created_at = models.DateTimeField(auto_now_add=True)
                       