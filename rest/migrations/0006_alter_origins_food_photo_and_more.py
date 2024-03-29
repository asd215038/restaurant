# Generated by Django 4.1.7 on 2023-10-11 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0005_alter_origins_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='origins_food',
            name='photo',
            field=models.ImageField(blank=True, default='img.jpg', upload_to='origins_food/'),
        ),
        migrations.AlterField(
            model_name='processing_plant',
            name='photo',
            field=models.ImageField(blank=True, default='img.jpg', upload_to='processing_plant/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, default='img.jpg', upload_to='product/'),
        ),
    ]
