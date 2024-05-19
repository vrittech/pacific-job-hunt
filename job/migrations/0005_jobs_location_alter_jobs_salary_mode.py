# Generated by Django 4.1 on 2024-05-15 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_jobs_salary_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='location',
            field=models.CharField(choices=[('on_site', 'Intern'), ('remote', 'Junior'), ('hybrid', 'Mid'), ('senior', 'Senior'), ('', '')], default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='salary_mode',
            field=models.CharField(choices=[('Annually', 'annually'), ('Hourly', 'hourly'), ('Monthly', 'monthly')], default='monthly', max_length=20),
        ),
    ]