# Generated by Django 2.2.28 on 2023-03-12 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_auto_20230312_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outcome',
            name='image',
            field=models.ImageField(blank=True, upload_to='outcome_images'),
        ),
    ]
