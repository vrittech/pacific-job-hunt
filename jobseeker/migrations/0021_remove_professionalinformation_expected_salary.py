# Generated by Django 4.1 on 2024-05-22 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0020_delete_jobsapply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professionalinformation',
            name='expected_salary',
        ),
    ]
