# Generated by Django 3.0.9 on 2020-08-04 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('institution', models.CharField(max_length=255)),
                ('employment_type', models.CharField(choices=[('Faculty', 'Faculty'), ('Researcher', 'Researcher'), ('Student', 'Student')], max_length=20)),
                ('application_purpose', models.TextField()),
            ],
        ),
    ]
