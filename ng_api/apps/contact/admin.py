from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'service', 'submitted_at')
    search_fields = ('last_name', 'email')
    list_filter = ('submitted_at',)
    ordering = ('-submitted_at',)