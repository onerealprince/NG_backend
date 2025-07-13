from django.urls import path
from .views import FaqsCreateView, FaqByServiceView, FaqsListView

urlpatterns = [
    path('faqs/', FaqsListView.as_view(), name='faq-list'),
    path('faqs/', FaqsCreateView.as_view(), name='faqs'),
    path('faqs/service/<str:service>/', FaqByServiceView.as_view(), name='faq-by-service'),

]
