# Generated by Django 3.0.9 on 2021-01-07 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20210107_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='facebook_url',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='twitter_url',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='website',
        ),
        migrations.AddField(
            model_name='teammember',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
