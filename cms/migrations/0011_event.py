# Generated by Django 3.0.9 on 2021-01-08 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='events')),
                ('title', models.CharField(max_length=255)),
                ('speaker', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('event_date', models.DateTimeField()),
                ('price', models.CharField(max_length=100)),
                ('registration_link', models.URLField()),
                ('venue', models.TextField()),
            ],
        ),
    ]
