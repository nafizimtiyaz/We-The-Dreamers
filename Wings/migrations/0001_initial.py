# Generated by Django 4.2 on 2024-02-06 12:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='wings/image')),
                ('description', models.TextField(max_length=500)),
                ('image2', models.ImageField(blank=True, null=True, upload_to='wings/image')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='wings/image')),
                ('description2', models.TextField(max_length=1000)),
                ('wings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Wings.wings')),
            ],
        ),
    ]
