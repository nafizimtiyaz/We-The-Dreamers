# Generated by Django 4.2 on 2024-02-09 17:39

import ckeditor.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_ouractivity_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='recent/activity')),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=1000, null=True)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=12)),
            ],
        ),
    ]
