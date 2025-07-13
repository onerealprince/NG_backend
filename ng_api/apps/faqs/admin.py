from django.contrib import admin
from .models import faqs

@admin.register(faqs)
class faqsAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'service')
    search_fields = ('service', 'created_at')
    list_filter = ('service', 'created_at')
