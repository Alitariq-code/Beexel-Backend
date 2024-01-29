from django.contrib import admin
from .models import Enroll, ContactUs, Blog

# Register your models here.

@admin.register(Enroll)
class EnrollAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_no', 'education', 'passing_out_year', 'enroll_course', 'resume']
    search_fields = ['first_name', 'last_name', 'email', 'phone_no', 'education', 'passing_out_year', 'enroll_course']


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'subject', 'message', 'date_time']
    search_fields = ['full_name', 'email', 'subject', 'message', 'date_time']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'category', 'date_time', 'description']
    search_fields = ['title', 'image', 'category', 'date_time', 'description']