from rest_framework import serializers
from home.models import Enroll, ContactUs, Blog


class EnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll
        fields = ['first_name', 'last_name', 'email', 'phone_no', 'education', 'passing_out_year', 'enroll_course', 'resume']


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'subject', 'message', 'date_time']


import re
def replace_line_breaks(input_string):
    # Use a regular expression with the re.sub() function to replace all occurrences
    replaced_string = re.sub(r'\r\n', '<br>', input_string)
    return replaced_string
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'image', 'category', 'date_time', 'description']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        exclude_description = self.context.get('exclude_description', False)
        # Exclude 'description' field if specified in the context
        if exclude_description:
            data.pop('description', None)
        return data
