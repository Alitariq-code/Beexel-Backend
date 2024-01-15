from rest_framework import serializers
from home.models import Enroll, ContactUs, Blog


class EnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll
        fields = ['first_name', 'last_name', 'email', 'phone_no', 'education', 'passing_out_year', 'enroll_course']


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'subject', 'message', 'date_time']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'category', 'date_time', 'description']