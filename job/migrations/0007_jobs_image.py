# Generated by Django 4.1 on 2024-05-15 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_jobs_expiry_date_alter_jobs_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='image',
            field=models.ImageField(null=True, upload_to='jobs/images'),
        ),
    ]
