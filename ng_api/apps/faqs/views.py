from rest_framework import generics
from .models import Faqs
from .serializers import FaqsSerializer

#Create FAQ
class FaqsCreateView(generics.CreateAPIView):
    queryset = Faqs.objects.all()
    serializer_class = FaqsSerializer

# List all FAQs
class FaqsListView(generics.ListAPIView):
    queryset = Faqs.objects.all()
    serializer_class = FaqsSerializer

# List FAQs by service
class FaqByServiceView(generics.ListAPIView):
    serializer_class = FaqsSerializer

    def get_queryset(self):
        service = self.kwargs['service']
        return Faqs.objects.filter(service__iexact=service) 