from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from home.models import Enroll, ContactUs, Blog
from .serializers import EnrollSerializer, ContactUsSerializer, BlogSerializer
from .google_sheet import google_sheet
from .send_email import send_email
from rest_framework.response import Response

class EnrollViewSet(viewsets.ModelViewSet):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer

    def perform_create(self, serializer):
        # Call the parent class's perform_create method to save the object to the database
        instance = serializer.save()
        options = {
        'type': 'apply',
        'data':{
        'first_name': instance.first_name,
        'last_name': instance.last_name,
        'email': instance.email,  # Replace with the recipient's email
        'phone_no': instance.phone_no,
        'education': instance.education,
        'passing_out_year': instance.passing_out_year,
        'enroll_course': instance.enroll_course,
        'resume': instance.resume,
        'resume_url': instance.resume.url if instance.resume else '',
        }
    }
        # google_sheet(options)
        send_email(options)

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    def perform_create(self, serializer):
        # Call the parent class's perform_create method to save the object to the database
        instance = serializer.save()
# Prepare options dictionary with data from the ContactUs instance
        options = {
         'type': 'contact',
         'data': {
              'full_name': instance.full_name,
             'email': instance.email,
            
            'message': instance.message,
         }
        }
        # Call the functions to send email and update Google Sheet
        send_email(options)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def list(self, request, *args, **kwargs):
        # Set context to exclude 'description' field
        serializer_context = {'request': request, 'exclude_description': True}
        serializer = self.get_serializer(self.queryset, many=True, context=serializer_context)
        return Response(serializer.data)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Set context to include all fields
        serializer_context = {'request': request, 'exclude_description': False}
        serializer = self.get_serializer(instance, context=serializer_context)
        return Response(serializer.data)
