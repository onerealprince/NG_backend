from django.urls import path
from .views import (
    TestimonialCreateView,
    TestimonialListView,
    TestimonialByServiceView
)

urlpatterns = [
    path('testimonials/', TestimonialListView.as_view(), name='testimonial-list'),
    path('testimonials/create/', TestimonialCreateView.as_view(), name='testimonial-create'),
    path('testimonials/service/<str:service>/', TestimonialByServiceView.as_view(), name='testimonial-by-service'),
]
