# Generated by Django 3.0.9 on 2020-08-06 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20200804_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
