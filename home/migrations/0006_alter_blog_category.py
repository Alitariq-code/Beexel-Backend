# Generated by Django 4.2.7 on 2024-02-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(blank=True, choices=[('data_science', 'Data Science'), ('data_engineering', 'Data Engineering'), ('machine_learning', 'Machine Learning'), ('deep_learning', 'Deep Learning')], max_length=200, null=True),
        ),
    ]
