# Generated by Django 4.2.4 on 2023-09-28 20:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watches', '0013_alter_item_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='main_image',
            field=cloudinary.models.CloudinaryField(default='your_default_cloudinary_url_here', max_length=255, verbose_name='main_image'),
        ),
    ]