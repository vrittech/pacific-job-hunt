# Generated by Django 4.1 on 2024-05-22 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0017_jobsbookmark_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mysocialmedia',
            name='social_media',
        ),
        migrations.RemoveField(
            model_name='mysocialmedia',
            name='user',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='job_categories',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='user',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='MySocialMedia',
        ),
        migrations.DeleteModel(
            name='WorkExperience',
        ),
    ]