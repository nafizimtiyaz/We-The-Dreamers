# Generated by Django 4.2.3 on 2024-03-09 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AboutUs', '0005_disastermanagementwig_image_educationwing_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disastermanagementwig',
            name='name',
        ),
        migrations.RemoveField(
            model_name='educationwing',
            name='name',
        ),
        migrations.RemoveField(
            model_name='medicalwings',
            name='name',
        ),
    ]