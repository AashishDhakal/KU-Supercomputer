# Generated by Django 3.0.9 on 2021-01-13 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_event_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-event_date',)},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-published_date',), 'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.CharField(default='', max_length=30),
        ),
    ]
