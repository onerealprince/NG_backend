from django.contrib import admin
from .models import Testimonial

# Register your models here.
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'created_at')
    search_fields = ('name', 'service')
    list_filter = ('service', 'created_at')