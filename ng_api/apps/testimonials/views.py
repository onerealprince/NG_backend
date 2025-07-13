from rest_framework import generics
from .models import Testimonial
from .serializers import TestimonialSerializer

# Create a new testimonial
class TestimonialCreateView(generics.CreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

# List all testimonials
class TestimonialListView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

# List testimonials by service
class TestimonialByServiceView(generics.ListAPIView):
    serializer_class = TestimonialSerializer

    def get_queryset(self):
        service = self.kwargs['service']
        return Testimonial.objects.filter(service__iexact=service)
