# Generated by Django 2.2.28 on 2023-03-09 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20230309_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
