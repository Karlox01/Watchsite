# Generated by Django 4.2.4 on 2023-09-28 20:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watches', '0014_alter_item_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='main_image',
            field=cloudinary.models.CloudinaryField(default='https://as2.ftcdn.net/v2/jpg/00/89/55/15/1000_F_89551596_LdHAZRwz3i4EM4J0NHNHy2hEUYDfXc0j.jpg', max_length=255, verbose_name='main_image'),
        ),
    ]
