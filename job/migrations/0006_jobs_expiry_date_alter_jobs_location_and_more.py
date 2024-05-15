# Generated by Django 4.1 on 2024-05-15 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_jobs_location_alter_jobs_salary_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='expiry_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobs',
            name='location',
            field=models.CharField(choices=[('on_site', 'on_site'), ('remote', 'remote'), ('hybrid', 'hybrid'), ('', '')], default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='timing',
            field=models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'contract')], default='full_time', max_length=20),
        ),
    ]
