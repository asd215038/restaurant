# Generated by Django 4.1.7 on 2023-10-07 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_alter_origins_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='origins',
            name='photo',
            field=models.ImageField(blank=True, default='img.jpg', upload_to='origins/'),
        ),
    ]