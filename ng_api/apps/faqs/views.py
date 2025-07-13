from rest_framework import generics
from .models import faqs
from .serializers import faqsSerializer

class faqsCreateView(generics.CreateAPIView):
    queryset = faqs.objects.all()
    serializer_class = faqsSerializer

class faqsListView(generics.ListAPIView):
    queryset = faqs.objects.all()
    serializer_class = faqsSerializer