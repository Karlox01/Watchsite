# Generated by Django 4.2.4 on 2023-09-24 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watches', '0008_item_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='has_box',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='has_papers',
            field=models.BooleanField(default=False),
        ),
    ]
