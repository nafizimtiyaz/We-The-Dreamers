# Generated by Django 4.2 on 2024-02-12 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_volunteer_volunteer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='present_organization',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]