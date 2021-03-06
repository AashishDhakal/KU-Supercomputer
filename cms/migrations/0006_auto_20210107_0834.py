# Generated by Django 3.0.9 on 2021-01-07 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_news_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='when',
        ),
        migrations.RemoveField(
            model_name='about',
            name='where',
        ),
        migrations.AddField(
            model_name='about',
            name='video_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='about',
            name='video_title',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='about',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='about'),
        ),
    ]
