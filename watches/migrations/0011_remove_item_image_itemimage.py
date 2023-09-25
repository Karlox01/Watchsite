# Generated by Django 4.2.4 on 2023-09-25 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watches', '0010_item_case_material_item_case_size_item_movement_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='item_images/')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='watches.item')),
            ],
        ),
    ]
