# Generated by Django 4.1 on 2024-06-03 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapply', '0003_alter_jobsapply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobsapply',
            name='is_saved_applicant',
            field=models.BooleanField(default=False),
        ),
    ]
