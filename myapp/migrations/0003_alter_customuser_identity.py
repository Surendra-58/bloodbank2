# Generated by Django 5.1.7 on 2025-04-17 16:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_customuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='identity',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='identity'),
        ),
    ]
