# Generated by Django 4.2.3 on 2024-03-09 14:35

import ckeditor.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('AboutUs', '0002_aboutactivity_disastermanagementwig_educationwing_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('image', models.ImageField(upload_to='Review')),
                ('name', models.TextField(max_length=200)),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='aboutactivity',
            name='name',
            field=ckeditor.fields.RichTextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='disastermanagementwig',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='educationwing',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='medicalwings',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='ourmission',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='ourvision',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=10000, null=True),
        ),
    ]
