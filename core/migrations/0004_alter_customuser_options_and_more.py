# Generated by Django 4.2 on 2024-02-12 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_volunteer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='leftest_degree',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='passing_year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
