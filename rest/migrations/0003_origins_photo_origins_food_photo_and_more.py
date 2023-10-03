# Generated by Django 4.1.7 on 2023-09-30 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_alter_booking_number_of_people_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='origins',
            name='photo',
            field=models.ImageField(blank=True, default='img.jpg', upload_to='upload/origins/'),
        ),
        migrations.AddField(
            model_name='origins_food',
            name='photo',
            field=models.ImageField(blank=True, default='img.jpg', upload_to='upload/origins_food/'),
        ),
        migrations.AddField(
            model_name='processing_plant',
            name='photo',
            field=models.ImageField(blank=True, default='img.jpg', upload_to='upload/processing_plant/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, default='img.jpg', upload_to='upload/product/'),
        ),
    ]
