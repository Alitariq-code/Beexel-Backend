from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from home.models import Enroll, ContactUs, Blog
from .serializers import EnrollSerializer, ContactUsSerializer, BlogSerializer


class EnrollViewSet(viewsets.ModelViewSet):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer