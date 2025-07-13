from django.urls import path
from .views import faqsCreateView

urlpatterns = [
    path('faqs/', faqsCreateView.as_view(), name='faqs'),
]
