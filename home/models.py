from django.db import models
from datetime import datetime
from markdownx.models import MarkdownxField

# Create your models here.

class Enroll(models.Model):
    first_name = models.CharField(max_length=300, null=True, blank=True)
    last_name = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField()
    phone_no = models.CharField(max_length=300, null=True, blank=True)
    education = models.CharField(max_length=300, null=True, blank=True)
    passing_out_year = models.CharField(max_length=300, null=True, blank=True)
    enroll_course = models.CharField(max_length=300, null=True, blank=True)
    resume = models.FileField(upload_to='resume_uploads/')



    def __str__(self):
        return self.first_name


class ContactUs(models.Model):
    full_name = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date_time = models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return self.email
    

class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('data_science', 'Data Science'),
        ('data_engineering', 'Data Engineering'),
        ('machine_learning', 'Machine Learning'),
        ('deep_learning', 'Deep Learning'),
       
    ]
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='')
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, null=True, blank=True)
    date_time = models.DateTimeField()
    description = models.TextField()