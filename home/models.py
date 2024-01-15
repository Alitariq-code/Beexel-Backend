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
        ('technique_training', 'Technique and Training'),
        ('industry_news', 'Industry News and Trends'),
        ('safety_responsibility', 'Safety and Responsibility'),
        ('competition_coverage', 'Competition Coverage'),
        ('historical_perspectives', 'Historical Perspectives'),
    ]
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='')
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, null=True, blank=True)
    date_time = models.DateTimeField()
    description = MarkdownxField()