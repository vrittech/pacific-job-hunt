# Generated by Django 4.1 on 2024-05-22 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0021_remove_professionalinformation_expected_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professionalinformation',
            name='position',
        ),
    ]
