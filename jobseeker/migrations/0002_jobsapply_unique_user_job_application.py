# Generated by Django 4.1 on 2024-05-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='jobsapply',
            constraint=models.UniqueConstraint(fields=('user', 'job'), name='unique_user_job_application'),
        ),
    ]