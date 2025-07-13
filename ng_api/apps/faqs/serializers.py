from rest_framework import serializers
from .models import faqs

class faqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = faqs
        fields = '__all__'